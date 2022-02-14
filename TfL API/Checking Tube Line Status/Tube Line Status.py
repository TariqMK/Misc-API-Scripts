import requests
import json

print(
    "\n" +
    "Which line do you want the status for?" +
    "\n" +
    "\n" + "Your options are:" +
    "\n" +
    "\n" + "District" +
    "\n" + "Central" +
    "\n" + "Circle" +
    "\n" + "Piccadilly" +
    "\n" + "Waterloo-City" +
    "\n" + "Bakerloo" +
    "\n" + "Hammersmith-City" +
    "\n" + "Jubilee" +
    "\n" + "Metropolitan" +
    "\n" + "Victoria" +
    "\n" + "Northern" +
    "\n"
    )
    
line = input()

reply = requests.get("https://api.tfl.gov.uk/Line/" + line + "/Status")

data = reply.json()

Status = (data[0]["lineStatuses"][0]["statusSeverityDescription"])

print(
    "\n" + "Line: " + line +
    "\n" + "Status: " + Status +
    "\n"
    )
