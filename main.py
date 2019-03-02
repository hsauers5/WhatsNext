from flask import (Flask,
    render_template,
    request,
    redirect,
    jsonify,
    session)
from http import HTTPStatus
import creds

# Use Flask / etc to design a REST API for WhatsNext back-end.
# get creds
GOOGLE_API = creds.get_google_creds()
YELP_API = creds.get_yelp_creds()

# Create the application instance
app = Flask(__name__, template_folder="")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return jsonify(HTTPStatus.OK)


@app.route('/find', methods=['GET'])
def find():
    if 'location' not in request.args:
        return jsonify(HTTPStatus.BAD_REQUEST)
    else:
        return jsonify(HTTPStatus.OK)


# start flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
