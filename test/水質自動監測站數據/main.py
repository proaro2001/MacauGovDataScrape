import requests

API_URL = "https://dspa.apigateway.data.gov.mo/T_Bas_Water_Monitor_Approved"
headers = {"Authorization": "APPCODE 09d43a591fba407fb862412970667de4"}
response = requests.post(API_URL, headers=headers)

if response.status_code == 200:
    for item in response.json():
        print(item)
else:
    print("Error occurred! Status code: ", response.status_code)
