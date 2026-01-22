import cv2
import time
import simpleaudio as sa


class DrowsinessDetector:
    def __init__(self):
        # Camera setup
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Load Haar cascades
        self.face_cascade = cv2.CascadeClassifier(
            "backend/models/haarcascade_frontalface_default.xml"
        )
        self.eye_cascade = cv2.CascadeClassifier(
            "backend/models/haarcascade_eye.xml"
        )

        # Drowsiness & blink logic
        self.start_time = None
        self.DROWSY_TIME = 2
        self.status = "AWAKE"

        self.blink_count = 0
        self.eye_closed = False

        # Performance optimization
        self.frame_count = 0

        # -------- ALARM (FINAL, RELIABLE LOGIC) --------
        self.alarm_wave = sa.WaveObject.from_wave_file(
            "backend/assets/alarm.wav"
        )
        self.last_alarm_time = 0
        self.ALARM_INTERVAL = 1.0  # seconds between beeps

    # ---------------- MAIN LOOP ----------------
    def generate_frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Resize for performance
            frame = cv2.resize(frame, (640, 480))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Run face detection every 5 frames
            self.frame_count += 1
            if self.frame_count % 5 == 0:
                faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            else:
                faces = []

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)

                # -------- Blink + drowsiness logic --------
                if len(eyes) >= 2:  # Eyes open
                    if self.eye_closed:
                        self.blink_count += 1
                        self.eye_closed = False

                    self.start_time = None
                    self.status = "AWAKE"
                    self.last_alarm_time = 0  # reset alarm timer

                else:  # Eyes closed
                    if not self.eye_closed:
                        self.eye_closed = True
                        self.start_time = time.time()
                    elif time.time() - self.start_time > self.DROWSY_TIME:
                        self.status = "DROWSY"

                        # ---- CONTINUOUS ALARM (TIME-BASED) ----
                        current_time = time.time()
                        if current_time - self.last_alarm_time >= self.ALARM_INTERVAL:
                            self.alarm_wave.play()
                            self.last_alarm_time = current_time

                # Draw face box
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # -------- Overlay text --------
            color = (0, 0, 255) if self.status == "DROWSY" else (0, 255, 0)
    

            # Encode frame for streaming
            _, buffer = cv2.imencode(
                ".jpg",
                frame,
                [int(cv2.IMWRITE_JPEG_QUALITY), 70]
            )

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" +
                   buffer.tobytes() + b"\r\n")
