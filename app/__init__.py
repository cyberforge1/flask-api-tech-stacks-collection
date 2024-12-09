# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Application factory for creating Flask app instances."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Validate configuration
    Config.validate()

    print("DEBUG (create_app): SQLALCHEMY_DATABASE_URI in config:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-RESTx API
    api = Api(
        app,
        version='1.0',
        title='Todo Management API',
        description='API documentation for Todo Management System',
        doc='/api/docs'  # Swagger UI available at /api/docs
    )

    # Import and register namespaces
    from .routes.todos import todos_bp
    from .routes.helloworld import helloworld_bp

    # Register namespaces with specific paths
    api.add_namespace(helloworld_bp, path='/api')
    api.add_namespace(todos_bp, path='/api/todos')

    return app
