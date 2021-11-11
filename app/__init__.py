from flask import Flask
from config import AppConfig


app = Flask(__name__)
app.config.from_object(AppConfig)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)
