from flask import Flask
from flask_cors import CORS
from .routes.schema_scoring_routes import score_schema_bp
from .utils.logging_config import configure_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = "some-unique-secret"

    # Important for cross-origin cookies in modern browsers
    app.config['SESSION_COOKIE_SAMESITE'] = 'None'
    app.config['SESSION_COOKIE_SECURE'] = False  # True requires HTTPS

    # Configure logging
    configure_logging(app)

    # Apply CORS globally with specific configuration
    CORS(
        app,
        resources={r"/*": {"origins": ["http://localhost:4200", "http://localhost:3000","*", "http://127.0.0.1:5000"]}},
        supports_credentials=True,
     #    allow_headers=["Content-Type", "Authorization"],
     #    expose_headers=["Content-Length", "X-Custom-Header"],
    )

    # Register Blueprints
    app.register_blueprint(score_schema_bp)


    return app

