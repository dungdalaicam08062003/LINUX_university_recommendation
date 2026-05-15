from flask import Blueprint, jsonify, Response
from communicate_Database import university
import json


bp = Blueprint("university", __name__, url_prefix="/university")


@bp.route("/data", methods=["GET"])
def get_university_data():
    university_info = university.get_university_info()
    return Response(
        json.dumps(university_info, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )
# @bp.route("/upload", methods=["POST"])
# def upload_sensor_data():
#     payload = request.json
#     return jsonify({"status": "ok", "received": payload})