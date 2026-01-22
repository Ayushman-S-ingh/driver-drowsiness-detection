const statusText = document.getElementById("status");
const blinkText = document.getElementById("blinks");

setInterval(async () => {
    try {
        const response = await fetch("/detect");
        const data = await response.json();

        // Update text
        statusText.innerText = data.status;
        blinkText.innerText = data.blinks;

        // Update color + animation
        if (data.status === "DROWSY") {
            statusText.className = "drowsy";
        } else {
            statusText.className = "awake";
        }

    } catch (error) {
        console.log("Waiting for backend...");
    }
}, 500);
