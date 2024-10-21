"""
MacauGovOpenSource is a parent class for all Macau Government
Open Source API. Since they all use the same authorization code, it
is easier to just put it in a parent class and inherit it.
"""

import requests
import csv
from datetime import date, datetime
import json
import csv
import os
from urllib.parse import urlparse


class MacauGovOpenSource:
    def __init__(self, API_URL="") -> None:
        self.API_URL = API_URL
        self.authorization = "APPCODE 09d43a591fba407fb862412970667de4"
        self.headers = {"Authorization": self.authorization}
        self.response = requests.get(self.API_URL, headers=self.headers)

    def downloadFile(self):
        # This function downloads file from the API_URL
        # and save it to the current directory
        # This function will encounter the following data type:
        # csv, json, xml, xlsx, xls, rdf

        content_type = self.response.headers["Content-Type"]
        with open("\data" + content_type, "wb") as file:
            file.write(self.response.content)

    # Turn json file to csv file
    def jsonToCsv(self, jsonFile, csvFile=date.today().strftime("%Y-%m-%d") + ".csv"):
        fieldnames = list(jsonFile[0].keys())
        # Save the data to a csv file with file name of today's date
        with open(csvFile, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jsonFile)
