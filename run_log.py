from flask import Flask, request
from flask_cors import CORS
import logging
import requests
import json
from routes import university

app = Flask(__name__)

# Load allowed origins from appsetting.json
with open("appsetting.json") as f:
    config = json.load(f)

CORS(app, origins=config["AllowedOrigins"])



# Cấu hình logging ra file
logging.basicConfig(filename="access.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

@app.before_request
def log_request_info():
    logging.info(f"Request from {request.remote_addr} "
                 f"{request.method} {request.path}")

@app.after_request
def log_response_info(response):
    logging.info(f"Response status: {response.status}")
    return response


class HttpLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post("http://100.68.174.55:9000/logs", json={"log": log_entry}, timeout=2)
        except Exception as e:
            print("Failed to send log:", e)

handler = HttpLogHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Register blueprints
app.register_blueprint(university.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
