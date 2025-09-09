from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)   # <--- this line is required
    CORS(app)

    # register blueprints
    from .api.comments import bp as comments_bp
    app.register_blueprint(comments_bp)

    return app
