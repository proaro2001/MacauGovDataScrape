"""
MacauGovOpenSource is a parent class for all Macau Government
Open Source API. Since they all use the same authorization code, it
is easier to just put it in a parent class and inherit it.
"""

import requests
import csv
from datetime import date, datetime
import json


class MacauGovOpenSource:
    def __init__(self, API_URL="") -> None:
        self.API_URL = API_URL
        self.authorization = "APPCODE 09d43a591fba407fb862412970667de4"
        self.headers = {"Authorization": self.authorization}
        self.response = None
        self.soup = None
        self.data = None

    # setters
    def setResponse(self, response):
        self.response = response

    def setAPI_URL(self, API_URL):
        self.API_URL = API_URL

    def setAuthorization(self, authorization):
        self.authorization = authorization

    def setHeaders(self, headers):
        self.headers = headers

    def setSoup(self, soup):
        self.soup = soup

    def setData(self, data):
        self.data = data

    # getters
    def getResponse(self):
        return self.response

    def getAPI_URL(self):
        return self.API_URL

    def getAuthorization(self):
        return self.authorization

    def getHeaders(self):
        return self.headers

    def getSoup(self):
        return self.soup

    def getData(self):
        return self.data

    # Turn json file to csv file
    def jsonToCsv(self, jsonFile, csvFile=date.today().strftime("%Y-%m-%d") + ".csv"):
        fieldnames = list(jsonFile[0].keys())
        # Save the data to a csv file with file name of today's date
        with open(csvFile, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jsonFile)
