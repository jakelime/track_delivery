import http.client
import json
import os
import urllib.parse

from dotenv import load_dotenv

load_dotenv()


params = urllib.parse.urlencode({"trackingNumber": "7777777770", "service": "express"})

headers = {"Accept": "application/json", "DHL-API-Key": os.environ.get("DHL_API_KEY")}

connection = http.client.HTTPSConnection("api-eu.dhl.com")

connection.request("GET", "/track/shipments?" + params, "", headers)
response = connection.getresponse()

status = response.status
reason = response.reason
data = json.loads(response.read())

print("Status: {} and reason: {}".format(status, reason))
print(data)

connection.close()
