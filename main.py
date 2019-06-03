"""Module for application factory."""

# Third-party libraries
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restplus import Api
from flask_cors import CORS
from flask_s3 import FlaskS3

from api import api_blueprint
from exception import exception_blueprint
from exception.validation import ValidationError
from config import config, AppConfig
from api.database import db
from api.bcrypt import bcrypt

api = Api(api_blueprint, doc=False)


s3 = FlaskS3()

def initialize_errorhandlers(application):
    ''' Initialize error handlers '''
    application.register_blueprint(exception_blueprint)
    application.register_blueprint(api_blueprint)


def create_app(config=AppConfig):
    """Return app object given config object."""
    #https://zappa-ok587zsna.s3.us-east-2.amazonaws.com
    kwargs = dict(
        template_folder='dist',
        static_folder='dist/static',
        # host_matching=True, 
        # static_host='https://zappa-ok587zsna.s3.us-east-2.amazonaws.com',
    )

    app = Flask(__name__, **kwargs)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config)

    app.url_map.strict_slashes = False

    # initialize error handlers
    initialize_errorhandlers(app)

    # bind app to db
    db.init_app(app)

    bcrypt.init_app(app)

    s3.init_app(app)

    import api.views

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app

@api.errorhandler(ValidationError)
@exception_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
