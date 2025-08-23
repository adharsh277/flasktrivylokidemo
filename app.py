from flask import Flask, request
import logging, sys

app = Flask(__name__)

logger = logging.getLogger("flask-app")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)

@app.route("/")
def hello():
    logger.info("Index hit from %s", request.remote_addr)
    return "Hello from Flask + Loki!\n"

@app.route("/error")
def oops():
    logger.error("Simulated error for demo")
    return ("Something went wrong\n", 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
