import creds

YELP_API = creds.get_yelp_creds()


# finds suggestions via yelp api
def find_suggestions(location, category, radius, money):
    # convert into meters for yelp api
    radius = convert_to_meters(radius)

    # dummy suggestions list
    suggestions = {'id':{'name':'thisname'}, 'newid':{'name':'newname'}}

    # query yelp api for suggestions

    return suggestions


# convert to meters for yelp api
def convert_to_meters(radius):
    return radius * 1609
