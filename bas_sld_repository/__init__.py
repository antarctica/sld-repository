import os

import sentry_sdk

from logging import Formatter
from logging.handlers import RotatingFileHandler

from flask import Flask, logging as flask_logging
# noinspection PyPackageRequirements
from werkzeug.utils import import_string


def create_app():
    app = Flask(__name__)

    config = import_string(f"bas_sld_repository.config.{str(os.environ['FLASK_ENV']).capitalize()}Config")()
    app.config.from_object(config)

    if 'LOGGING_LEVEL' in app.config:
        app.logger.setLevel(app.config['LOGGING_LEVEL'])
        flask_logging.default_handler.setFormatter(Formatter(app.config['LOG_FORMAT']))
    if app.config['APP_ENABLE_FILE_LOGGING']:
        file_log = RotatingFileHandler(app.config['LOG_FILE_PATH'], maxBytes=5242880, backupCount=5)
        file_log.setLevel(app.config['LOGGING_LEVEL'])
        file_log.setFormatter(Formatter(app.config['LOG_FORMAT']))
        app.logger.addHandler(file_log)

    if app.config['APP_ENABLE_SENTRY']:
        app.logger.info('Sentry error reporting enabled')
        sentry_sdk.init(**app.config['SENTRY_CONFIG'])

    app.logger.info(f"{app.config['NAME']} ({app.config['VERSION']}) [{app.config['ENV']}]")

    return app
