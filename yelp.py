import creds
import requests
import json

YELP_API = "Bearer " + creds.get_yelp_creds()
API_URL = "https://api.yelp.com/v3/businesses/search"

"""
term: category
location: literal address
rating: 4 (literal)
radius: meters
price: money
limit: # of results to return

auth: bearer token, from YELP_API
"""


# finds suggestions via yelp api
def find_suggestions(location, category, radius, money):
    # convert into meters for yelp api
    radius = convert_to_meters(radius)

    params = {
        'term': category,
        'location': location,
        'radius': radius,
        'price': money,
        'limit': 10
    }

    req = requests.get(url=API_URL, params=params, headers={"Authorization": YELP_API})
    content = req.content
    # print(content)

    biz = json.loads(content)
    print(biz['businesses'])

    # dummy suggestions list
    suggestions = {'id':{'name':'thisname'}, 'newid':{'name':'newname'}}

    # query yelp api for suggestions

    return suggestions


# convert to meters for yelp api
def convert_to_meters(radius):
    return radius * 1609
