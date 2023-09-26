from datasetsCrawler import DataExtractor

if __name__ == "__main__":
    extractor = DataExtractor()
    # extractor.printDataBy()

    print("----------------------")

    extractor.sort_by()
    # extractor.printDataBy()

    apis = extractor.getAPI()
