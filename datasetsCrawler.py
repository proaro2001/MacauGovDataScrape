"""
This py file extracts the api links from the data.csv file 
and stores it in the class variable apiLinks.
"""
import csv


class DataExtractor:
    def __init__(self, file="data.csv") -> None:
        self.file = file
        self.data = []
        self.api = []  # store api links
        self.initData(file)
        self.intiAPI()

    # Declaring private method
    def initData(self, file="data.csv"):
        with open(file, encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        self.data = data

    # Declaring private method
    def intiAPI(self):
        self.api.clear()
        for i in self.data:
            self.api.append(i["目録API"])

    def getData(self):
        return self.data

    def getAPI(self):
        self.intiAPI()
        return self.api

    # Declaring private method
    def merge_sort(self, data, determine="數據格式"):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = data[:mid]  # [0, mid)
        right = data[mid:]  # [mid, end)

        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)

        return self.merge(left=left_sorted, right=right_sorted, determine=determine)

    # Declaring private method
    def merge(self, left, right, determine="數據格式"):
        merged = []  # sorted list to be returned

        # index to indicate current position of each list
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][determine] <= right[right_index][determine]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    # Declaring private method
    def quick_sort(self, data, determine="數據格式"):
        if len(data) <= 1:
            return data

        pivot = len(data) // 2  # use // to get integer instead of float
        left = [x for x in data if x[determine] < data[pivot][determine]]
        middle = [x for x in data if x[determine] == data[pivot][determine]]
        right = [x for x in data if x[determine] > data[pivot][determine]]

        return (
            self.quick_sort(data=left, determine=determine)
            + middle
            + self.quick_sort(data=right, determine=determine)
        )

    def sort_by(self, determine="數據格式", method="merge"):
        if method == "quick":
            self.data = self.quick_sort(self.data, determine=determine)
        elif method == "merge":
            self.data = self.merge_sort(self.data, determine=determine)
        else:
            self.log("wrong method")

    def printDataBy(self, determine="數據格式"):
        for i in self.data:
            print(i[determine])
