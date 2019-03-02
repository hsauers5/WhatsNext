import creds
import requests
import json

GOOGLE_API = "Bearer " + creds.get_google_creds()
API_URL = "https://api.yelp.com/v3/businesses/search"


# posts data to firebase from dictionary
def post_to_firebase(data):
    # post to firebase
    print("posting: " + str(data))

