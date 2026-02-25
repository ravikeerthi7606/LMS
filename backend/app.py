from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import mongo, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from routes.auth_routes import auth_bp
    from routes.course_routes import course_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(course_bp, url_prefix="/api/courses")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    