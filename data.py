from xmlrpc.client import boolean

import requests

#   parameters given to access the API
parameters ={
    "amount": 20,
    "type": "boolean",
}


#Get API and add your parameters
response = requests.get("https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
data = response.json()
# print(data)
question_data = data["results"]
