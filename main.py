from flask import (Flask,
    request,
    jsonify)
from flask_api import status
import yelp

# Use Flask / etc to design a REST API for WhatsNext back-end.

# Create the application instance
app = Flask(__name__, template_folder="")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return jsonify(status.HTTP_200_OK)


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


@app.route('/categories', methods=['GET'])
def categories():
    categories = [
        "american",
        "seafood",
        "asian",
        "latin american",
        "vegan friendly",
        "breakfast",
        "pasta"
    ]
    return categories


# start flask application
if __name__ == '__main__':
    # yelp.find_suggestions('orlando', 'burgers', 5, 2)
    app.run(debug=False, host='0.0.0.0')
