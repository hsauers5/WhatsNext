import creds

YELP_API = creds.get_yelp_creds()


# finds suggestions via yelp api
def find_suggestions(location, category, radius, money):
    # dummy suggestions list
    suggestions = {'id':{'name':'thisname'}, 'newid':{'name':'newname'}}
    # query yelp api for suggestions
    return suggestions
