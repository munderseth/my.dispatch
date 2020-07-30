import sys
import requests
import os
import json
import time

REPO = "test"
BRANCH = "b1"
WF = "test.yml"

url    = "https://api.github.com/repos/munderseth/"+REPO
url2   = "https://api.github.com/repos/munderseth/"+REPO+"/dispatches"
url3   = "https://api.github.com/repos/munderseth/"+REPO+"/actions/workflows/"+WF+"/runs"

GH_TOKEN  = os.getenv('GH_TOKEN')

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.github.everest-preview+json",
    'Authorization': 'Token ' + GH_TOKEN,
  }

input = {'default_branch' : BRANCH}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)

input2 = {      
  "event_type": "testspace",
  "client_payload": {"function": "foo", "param1": "tbd"}
}

def main():
  global input


input = {'default_branch' : BRANCH}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)
print(response.status_code)

payload = json.dumps(input2)
# print(payload)
  
response = requests.request("POST", url2, data=payload, headers=headers)
print(response.status_code)

input = {'default_branch' : "master"}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)
print(response.status_code)

time.sleep(10)

response = requests.request("GET", url3, headers=headers)
print(response.status_code)
data = response.json()
print(data)

if __name__ == "__main__":  # pragma: no cover
    main()

