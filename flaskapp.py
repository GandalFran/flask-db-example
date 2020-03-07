from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound

from config import APP_NAME
from SQLUtils.SQLUtils import SQL

# flask configuration
app = Flask(APP_NAME)
app.config.from_object('config')
api = Api(app, version=app.config['VERSION'], title=app.config['TITLE'], description=app.config['DESCRIPTION'])
sql_service = api.namespace('v1', description=app.config['DESCRIPTION'])

# flask anti CORS policy configuration
CORS(app)

# instance my SQLUtils wrapper
sql_db = SQL(app.config['SQL_HOST'], app.config['SQL_DB'], app.config['SQL_USER'], app.config['SQL_PASSWORD'])


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


@sql_service.route("/")
class CheckStatus(Resource):
    """check status"""

    def get(self):
        return {"status": "OK"}


# define endpoint args parser
sql_insert_args_parser = reqparse.RequestParser()
sql_insert_args_parser.add_argument('data', required=True, type=str, location='form', help='missing data parameter')
sql_insert_args_parser.add_argument('origin', required=True, type=str, location='form', help='missing origin parameter')
sql_insert_args_parser.add_argument('data_type', required=True, type=str, location='form', help='missing data_type parameter')


@sql_service.route("/insert")
@sql_service.doc(
    params={'data': 'A json with data to insert', 'data_type': 'str with data type', 'origin': 'str with sensor id'})
class SQLInsert(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = sql_insert_args_parser

    @api.expect(sql_insert_args_parser)
    def post(self):
        """insert data in db"""
        data, data_type, origin = self._get_args()
        status = self._insert_db(data, data_type, origin)
        return {
            "status": status
        }

    def _get_args(self):
        args = self.parser.parse_args()
        data = args['data']
        origin = args['origin']
        data_type = args['data_type']
        return data, data_type, origin

    @classmethod
    def _insert_db(cls, data, data_type, origin):
        sql_db.insert(data, data_type, origin)
        return "OK"
