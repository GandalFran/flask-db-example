import os
import logging

# author and license information
AUTHOR = 'Example Examplus Examplicus'
AUTHOR_EMAIL = 'example@example.ex'
LICENSE = 'see license.md file for details'

# log configuration
DEBUG = True
LOG_LEVEL = logging.DEBUG

# flask configuration
PORT = 8080
HOST = '0.0.0.0'  # bind to all interfaces
TITLE = 'flask-SQLUtils-example'
VERSION = '1.0'
APP_NAME = 'flask-SQLUtils-example'
DESCRIPTION = 'Example to use flask and SQLUtils'

# SQLUtils configuration
SQL_HOST = 'localhost'
SQL_DB = 'SENSOR_EXAMPLE'
SQL_USER = 'sensor_ingest'
SQL_PASSWORD = '1234'

# application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
