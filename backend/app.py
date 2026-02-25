from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from config import Config
from flask_cors import CORS




app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# ----------------------
# Register Route
# ----------------------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "student")  # default role

    if not name or not email or not password:
        return jsonify({"message": "All fields required"}), 400

    if mongo.db.users.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    mongo.db.users.insert_one({
        "name": name,
        "email": email,
        "password": hashed_pw,
        "role": role
    })

    return jsonify({"message": "User registered successfully"}), 201



# ----------------------
# Login Route
# ----------------------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})

    if user and bcrypt.check_password_hash(user["password"], password):
        access_token = create_access_token(identity=email)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401


# ----------------------
# Protected Route
# ----------------------
@app.route('/api/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Welcome {current_user}"}), 200


if __name__ == "__main__":
    app.run(debug=True)