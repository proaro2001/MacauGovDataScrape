import requests
import json
import matplotlib.pyplot as plt
import csv

from macauGovApi import MacauGovOpenSource

# API_URL = "https://aacm.apigateway.data.gov.mo/api/open/listAircraftMovementStatistic"
# headers = {"Authorization": "APPCODE 09d43a591fba407fb862412970667de4"}

# response = requests.get(API_URL, headers=headers)
# if response.status_code == 200:
#     # load the json file into a python object
#     data = response.json()
#     keys = list(data[0].keys())

#     jsonToCsv(data, "data.csv")


# else:
#     # Handle the request error
#     print("Request error:", response.status_code)

if __name__ == "__main__":
    API_URL = (
        "https://aacm.apigateway.data.gov.mo/api/open/listAircraftMovementStatistic"
    )
    crawler = MacauGovOpenSource(API_URL)
    crawler.setResponse(requests.get(API_URL, headers=crawler.getHeaders()))
    if crawler.getResponse().status_code == 200:
        crawler.setData(crawler.getResponse().json())
        crawler.jsonToCsv(crawler.getData())
    else:
        print("Request error:", crawler.getResponse().status_code)
