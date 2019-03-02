# manage credentials


def get_google_creds():
    with open("googleapi.txt") as creds:
        google_api = creds.readlines()[0]
        if '\n' in google_api:
            google_api.replace('\n', '')
    return google_api


def get_yelp_creds():
    with open("yelpapi.txt") as creds:
        yelp_api = creds.readlines()[0].replace('\n', '')
    return yelp_api
