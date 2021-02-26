import sys
import requests
import os
import json
import time

REPO = "my.dispatch"
DEFAULT = "master"
BRANCH = "the.branch"

url    = "https://api.github.com/repos/munderseth/"+REPO
url2   = "https://api.github.com/repos/munderseth/"+REPO+"/dispatches"

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

input = {'default_branch' : DEFAULT}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)
print(response.status_code)

SEC=1
print("sleep ..", SEC)
time.sleep(SEC)

payload = json.dumps(input2)
response = requests.request("POST", url2, data=payload, headers=headers)
print(response.status_code)

if __name__ == "__main__":  # pragma: no cover
    main()

