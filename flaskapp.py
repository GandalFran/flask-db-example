from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound

from config import APP_NAME
from MongoDBUtils.MongoDBUtils import MongoDB

# flask configuration
app = Flask(APP_NAME)
app.config.from_object('config')
api = Api(app, version=app.config['VERSION'], title=app.config['TITLE'], description=app.config['DESCRIPTION'])
mongodb_service = api.namespace('v1', description=app.config['DESCRIPTION'])

# flask anti CORS policy configuration
CORS(app)

# instance my SQLUtils wrapper
mongoDB = MongoDB(app.config['MONGO_URI'], app.config['MONGO_DB'])


# error handling
@api.errorhandler(BadRequest)
def handle_bad_request_exception(error):
    return {"message": str(error)}, 403


@api.errorhandler(NotFound)
def handle_not_found_exception(error):
    return {"message": str(error)}, 404


@api.errorhandler
def default_error_handler(error):
    return {"message": str(error)}, 500


@mongodb_service.route("/")
class CheckStatus(Resource):
    """check status"""

    def get(self):
        return {"status": "OK"}


# define endpoint args parser
argument_parser = reqparse.RequestParser()
argument_parser.add_argument('data', required=True, type=str, location='json', help='missing data parameter')
argument_parser.add_argument('sensor', required=True, type=str, location='json', help='missing sensor parameter')


@mongodb_service.route("/insert")
@mongodb_service.doc(
    params={'data': 'A json with data to insert', 'sensor': 'The sensor ID'})
class SQLInsert(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = argument_parser

    @api.expect(argument_parser)
    def post(self):
        """insert data in db"""
        data, sensor = self._get_args()
        status = self._insert_db(sensor, data)
        return {
            "status": status
        }

    def _get_args(self):
        args = self.parser.parse_args()
        data = args['data']
        sensor = args['sensor']
        return data, sensor

    @classmethod
    def _insert_db(cls, sensor, data):
        document = {
            "timestamp": datetime.today(),
            "sensor": sensor,
            "sample": data
        }
        mongoDB.insert(app.config['MONGO_COLLECTION'], document)
        return "OK"
