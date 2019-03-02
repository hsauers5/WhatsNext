# Use Flask / etc to design a REST API for WhatsNext back-end.
# get creds
GOOGLE_API = ""
with open("googleapi.txt") as creds:
    GOOGLE_API = creds.readlines()[0]
    if '\n' in GOOGLE_API:
        GOOGLE_API.replace('\n', '')
print(GOOGLE_API)

YELP_API = ""
with open("yelpapi.txt") as creds:
    YELP_API = creds.readlines()[0]
    if '\n' in YELP_API:
        YELP_API.replace('\n', '')
print(YELP_API)
