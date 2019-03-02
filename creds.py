# manage credentials

def get_google_creds():
    with open("googleapi.txt") as creds:
        GOOGLE_API = creds.readlines()[0]
        if '\n' in GOOGLE_API:
            GOOGLE_API.replace('\n', '')
    return GOOGLE_API


def get_yelp_creds():
    with open("yelpapi.txt") as creds:
        YELP_API = creds.readlines()[0]
        if '\n' in YELP_API:
            YELP_API.replace('\n', '')
    return YELP_API