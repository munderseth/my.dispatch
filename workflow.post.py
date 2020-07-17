import sys
import requests
import os
import json

BRANCH="master"

url      = "https://api.github.com/repos/munderseth/my.dispatch/actions/workflows/wf.yml/dispatches"
GH_TOKEN  = os.getenv('GH_TOKEN')

headers = {
  'Content-Type': "application/json",
  'Accept': "application/vnd.github.v3+json",
  'Authorization': 'Token ' + GH_TOKEN,
}

data = {
  "ref": BRANCH,
  "inputs": {"p1": "py"} 
}

def main():
 
  payload = json.dumps(data)
  print(payload)
  
  response = requests.request("POST", url, data=payload, headers=headers)
  print(response.status_code)

if __name__ == "__main__":  # pragma: no cover
    main()
