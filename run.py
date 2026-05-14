from flask import Flask
from flask_cors import CORS
import json
from routes import university

app = Flask(__name__)

# Load allowed origins from appsetting.json
with open("appsetting.json") as f:
    config = json.load(f)

CORS(app, origins=config["AllowedOrigins"])

# Register blueprints
app.register_blueprint(university.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
