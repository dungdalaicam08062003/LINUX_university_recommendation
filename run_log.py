from flask import Flask, request
from flask_cors import CORS
import logging
import requests
import json
from routes import university

app = Flask(__name__)

# Load allowed origins từ appsetting.json
with open("appsetting.json") as f:
    config = json.load(f)

CORS(app, origins=config["AllowedOrigins"])

# --- Cấu hình logging ---
# Ghi file
logging.basicConfig(filename="access.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

# In ra console
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

@app.before_request
def log_request_info():
    logging.info(f"Request from {request.remote_addr} "
                 f"{request.method} {request.path}")

@app.after_request
def log_response_info(response):
    logging.info(f"Response status: {response.status}")
    return response

# --- Gửi log sang node khác ---
class HttpLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post("http://192.168.207.133:5000/logs",
                          json={"log": log_entry}, timeout=2)
        except Exception as e:
            print("Failed to send log:", e)

http_handler = HttpLogHandler()
http_handler.setFormatter(formatter)
logging.getLogger().addHandler(http_handler)

# Register blueprints
app.register_blueprint(university.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
