from datasetsCrawler import DataExtractor
from macauGovApi import MacauGovOpenSource
import requests

if __name__ == "__main__":
    # extractor = DataExtractor()
    # # extractor.printDataBy()

    # print("----------------------")

    # extractor.sort_by()
    # # extractor.printDataBy()

    # apis = extractor.getAPI()

    API_URL = "https://api.data.gov.mo/document/download/ffa03c4b-cb93-4d27-b82f-6fd05ed87f31?token=null&isNeedFile=0&lang=TC"
    mc = MacauGovOpenSource(API_URL)
    mc.downloadFile()
