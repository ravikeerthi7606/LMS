from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import mongo

course_bp = Blueprint("courses", __name__)

@course_bp.route("/", methods=["POST"])
@jwt_required()
def create_course():
    data = request.json
    mongo.db.courses.insert_one(data)
    return jsonify({"msg": "Course created"})


@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = list(mongo.db.courses.find({}, {"_id": 0}))
    return jsonify(courses)