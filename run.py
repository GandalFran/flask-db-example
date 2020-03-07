import logging
from flaskapp import app
from config import HOST, PORT, LOG_LEVEL

if __name__ == "__main__":
    logging.basicConfig(level=LOG_LEVEL)
    app.run(host=HOST, port=PORT)
