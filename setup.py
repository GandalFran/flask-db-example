from setuptools import setup
from config import APP_NAME, VERSION, DESCRIPTION, AUTHOR, AUTHOR_EMAIL, LICENSE

setup(
    name=APP_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url="http://localhost:8080",
    packages=['extraction'],
    install_requires=[
        'Flask==1.1.1',
        'werkzeug==0.16.1',
        'flask_cors==3.0.8',
        'flask_restplus==0.13.0',
        'mysql-connector-python==8.0.11', 'mysql'
    ]
)
