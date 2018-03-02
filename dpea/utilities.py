import requests
import base64
import json

class MixPanel(object):
    MIXPANEL_URL = "http://api.mixpanel.com/track/?data="
    properties = {}

    def __init__(self, projectName, token):
        self.properties.clear()
        self.addProperty("token", token)
        self.addProperty("distinct_id", projectName)

    def setEventName(self, eventName):
        self.eventName = eventName

    def addProperty(self, key, value):
        self.properties[key] = value

    def sendEvent(self):
        event = {}
        event['event'] = self.eventName;
        event['properties'] = self.properties

        data = json.dumps(event)
        url = self.MIXPANEL_URL + base64.b64encode(data.encode("utf-8")).decode("utf-8");
        requests.post(url)

