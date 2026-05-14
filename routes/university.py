from flask import Blueprint, request, jsonify
from communicate_Database import university


bp = Blueprint("university", __name__, url_prefix="/university")

@bp.route("/data", methods=["GET"])
def get_university_data():
    university_info = university.get_university_info()
    return jsonify(university_info)


# @bp.route("/upload", methods=["POST"])
# def upload_sensor_data():
#     payload = request.json
#     return jsonify({"status": "ok", "received": payload})