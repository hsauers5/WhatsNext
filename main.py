from flask import (Flask,
    render_template,
    request,
    redirect,
    jsonify,
    session)
from http import HTTPStatus
import creds
import yelp

# Use Flask / etc to design a REST API for WhatsNext back-end.

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
    elif 'category' not in request.args:
        return jsonify(HTTPStatus.BAD_REQUEST)
    elif 'radius' not in request.args:
        return jsonify(HTTPStatus.BAD_REQUEST)
    elif 'money' not in request.args:
        return jsonify(HTTPStatus.BAD_REQUEST)
    else:
        location = request.args['location']
        category = request.args['category']
        radius = int(request.args['radius'])
        money = int(request.args['money'])
        return jsonify(yelp.find_suggestions(location=location, category=category, radius=radius, money=money))


# start flask application
if __name__ == '__main__':
    yelp.find_suggestions('orlando', 'burgers', 5, 2)
    # app.run(debug=False, host='0.0.0.0')
