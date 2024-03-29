import sys
import requests
import os
import json
import time

REPO    = "my.dispatch"
DEFAULT = "master"
BRANCH  = "the.branch"

url    = "https://api.github.com/repos/munderseth/"+REPO
url2   = "https://api.github.com/repos/munderseth/"+REPO+"/dispatches"

GH_TOKEN  = os.getenv('GH_TOKEN')

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.github.everest-preview+json",
    'Authorization': 'Token ' + GH_TOKEN,
  }

def main():
  global input

################################################
# SET default = BRANCH
################################################

input = {'default_branch' : BRANCH}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)
print(response.status_code)

###############################################
# DELAY ..
###############################################

SEC=0
print("sleep after branch poked..", SEC)
time.sleep(SEC)

################################################
# POST REPO DISPATCH
################################################

input2 = {      
  "event_type": "testspace",
  "client_payload": {"function": "foo", "param1": "tbd"}
}

payload = json.dumps(input2)
response = requests.request("POST", url2, data=payload, headers=headers)
print(response.status_code)

###############################################
# DELAY ..
###############################################

SEC=3
print("sleep after branch poked..", SEC)
time.sleep(SEC)

################################################
# SET default = master/main
################################################

input = {'default_branch' : DEFAULT}
newbranch = json.dumps(input)
response = requests.request("PATCH", url, data=newbranch, headers=headers)
print(response.status_code)

if __name__ == "__main__":  # pragma: no cover
    main()

