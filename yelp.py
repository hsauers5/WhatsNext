import creds
import requests
import json

YELP_API = "Bearer " + creds.get_yelp_creds()
API_URL = "https://api.yelp.com/v3/businesses/search"
MIN_RATING = 3.8


# finds suggestions via yelp api
def find_suggestions(location, category, radius, money, is_open=True):
    # convert into meters for yelp api
    radius = convert_to_meters(radius)

    money_arr = []
    for i in range(1, money+1):
        money_arr.append(i)

    params = {
        'term': category,
        'location': location,
	'categories': 'restaurants',
        'radius': radius,
        'price': money_arr,
        'limit': 10,
        'open_now': is_open
    }

    try:
        req = requests.get(url=API_URL, params=params, headers={"Authorization": YELP_API})
        content = req.content.decode('utf-8')
        # print(type(content))

        biz = json.loads(content)['businesses']

        results = []
        for business in biz:
            if float(business['rating']) > MIN_RATING:
                results.append(business)

        # dummy suggestions list
        suggestions = {'id':{'name':'thisname'}, 'newid':{'name':'newname'}}

        # print(results)

        final = []
        for business in results:
            biz = {'name': business['name'], 'phone': business['display_phone'], 'price': business['price'],
                     'image': business['image_url'], 'rating': business['rating'],
                     'address': business['location']['display_address'][0] + " " + business['location']['display_address'][1]}
            final.append(biz)

        return final
    except IndexError:
        return []
    except:
        return []


# convert to meters for yelp api
def convert_to_meters(radius):
    return radius * 1609
