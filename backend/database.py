from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["course_app"]

users_collection = db["users"]
courses_collection = db["courses"]
purchases_collection = db["purchases"]