from flask import Flask
import logging

APP = Flask(__name__)
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@APP.route('/')
def hello_world():
    LOGGER.info("This function is called")
    return {"message": "My webhook for the PD POC"}, 200

if __name__ == '__main__':
    APP.run(debug=True)