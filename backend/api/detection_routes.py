from flask import Blueprint, jsonify, Response
from backend.services.drowsiness_detector import DrowsinessDetector

detection_bp = Blueprint("detection", __name__)
detector = DrowsinessDetector()

@detection_bp.route("/detect")
def detect():
    return jsonify({
        "status": detector.status,
        "blinks": detector.blink_count
    })

@detection_bp.route("/video_feed")
def video_feed():
    return Response(
        detector.generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )
