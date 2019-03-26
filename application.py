import logging
import os
from multiplayer import application
logger = logging.getLogger(__name__)


@application.route('/', methods=['GET'])
def default_route():
    application.logger.info("base url requested. saying hello")
    return "Hi. My name is robot."


if __name__ == "__main__":
    # application.run()
    application.run(host= '0.0.0.0', port=9000, debug=False)
    # app.run(debug=True)
