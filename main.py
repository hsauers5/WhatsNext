import sys
from flask import (Flask,
                   request,
                   jsonify,
                   render_template, url_for)
from flask_api import status
import yelp

# Use Flask / etc to design a REST API for WhatsNext back-end.

# Create the application instance
app = Flask(__name__, template_folder="", static_url_path='/static')

ENDPOINTS = [
    "GET /",
    "GET /find PARAMS location, category, radius, money, open",
    "GET /categories"
]


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return jsonify(ENDPOINTS), status.HTTP_200_OK


@app.route('/find', methods=['GET'])
def find():
    if 'location' not in request.args:
        return "Bad request. Check params.", status.HTTP_400_BAD_REQUEST
    elif 'category' not in request.args:
        return "Bad request. Check params.", status.HTTP_400_BAD_REQUEST
    elif 'radius' not in request.args:
        return "Bad request. Check params.", status.HTTP_400_BAD_REQUEST
    elif 'money' not in request.args:
        return "Bad request. Check params.", status.HTTP_400_BAD_REQUEST
    else:
        location = request.args['location']
        category = request.args['category']
        radius = int(request.args['radius'])
        money = int(request.args['money'])

        open = True
        if 'open' in request.args:
            if request.args['open'] == 'False' or request.args['open'] == "false":
                open = False

        restaurants = yelp.find_suggestions(location=location, category=category, radius=radius, money=money, is_open=open)

        if len(restaurants) == 0:
            return "None found.", status.HTTP_400_BAD_REQUEST
        else:
            return jsonify(restaurants), status.HTTP_200_OK


CATEGORY_LIST = [
        "american",
        "seafood",
        "asian",
        "latin american",
        "vegan friendly",
        "breakfast",
        "pasta"
    ]


@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(CATEGORY_LIST)


@app.route('/images', methods=['GET'])
def images():
    if 'name' not in request.args:
        return "Bad request. Check image name.", status.HTTP_400_BAD_REQUEST
    else:
        name = request.args['name']
        img_filename = 'img.png'

        if name == 'american':
            img_filename = 'burger.png'

        return request.host_url[:-1] + url_for('static', filename=img_filename)

# start flask application
if __name__ == '__main__':
    # yelp.find_suggestions('orlando', 'burgers', 5, 2)
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(debug=False, host='0.0.0.0', port=port)
