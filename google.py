import creds
import requests
import json

GOOGLE_API = "Bearer " + creds.get_google_creds()
API_URL = "https://api.yelp.com/v3/businesses/search"


# fetches today's datetime via external api to avoid server confusion
def get_datetime():
    date_url = "http://worldclockapi.com/api/json/est/now"
    contents = json.loads(urllib.request.urlopen(date_url).read())
    date = contents['currentDateTime']
    return date


# posts data to firebase from dictionary
def post_to_firebase(data):
    # post to firebase
    print("posting: " + str(data))

    date = get_datetime()
    biz_name = data['bizname']
    address = data['address']
    category = data['category']
    price = data['price']
    userdata = data['userdata']
    
    # not really firebase, just a local csv
    # append to csv
    with open('log.csv', 'a') as fd:
        fd.write(date + "," + biz_name + "," + address + "," + category + "," + price + "," + userdata + '\n')

