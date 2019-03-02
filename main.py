# Use Flask / etc to design a REST API for WhatsNext back-end.
GOOGLE_API = ""
with open("googleapi.txt") as creds:
    GOOGLE_API = creds.readlines()[0]
    if '\n' in GOOGLE_API:
        GOOGLE_API.replace('\n', '')
print(GOOGLE_API)

