import http.client
import json
import os
import urllib.parse
import datetime
from dotenv import load_dotenv

load_dotenv()


def get_current_dt(dtfmtstr: str = "%Y%m%d_%H%M%S", append_us: bool = True):
    now = datetime.now()
    timestr = now.strftime()
    if append_us:
        timestr_ms = now.strftime("%f")[:2]
        timestr = f"{timestr}{timestr_ms}"
    return timestr


params = urllib.parse.urlencode({"trackingNumber": "2819479703", "service": "express"})

headers = {"Accept": "application/json", "DHL-API-Key": os.environ.get("DHL_API_KEY")}

connection = http.client.HTTPSConnection("api-eu.dhl.com")

connection.request("GET", "/track/shipments?" + params, "", headers)
response = connection.getresponse()

status = response.status
reason = response.reason
data = json.loads(response.read())

print("Status: {} and reason: {}".format(status, reason))
print(f"{len(data)=}")
with open("results.json", "w") as out_file:
    json.dump(data, out_file, indent=6)
    
connection.close()
