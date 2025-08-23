import logging
import sys
from flask import Flask, request

app = Flask(__name__)

# Configure logging (both stdout + file)
logger = logging.getLogger("flask-app")
logger.setLevel(logging.INFO)

# Console handler (stdout for Docker logs)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(console_handler)

# File handler (for promtail to read)
file_handler = logging.FileHandler("/var/log/flask_app.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(file_handler)

@app.route("/")
def hello():
    logger.info("Hello endpoint was hit from %s", request.remote_addr)
    return "Hello, World!"

@app.route("/error")
def error():
    logger.error("Simulated error triggered")
    return "Something went wrong!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
