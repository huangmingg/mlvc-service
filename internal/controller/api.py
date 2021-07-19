from flask_restful_swagger import swagger
from flask_restplus import Api
import logging

log = logging.getLogger(__name__)

api = swagger.docs(Api(
    version="1.0",
    title="MLVC Service",
    validate=True))

@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred, please check the logs for more information."
    log.exception(message, e)
    return {"message": message}, 500

