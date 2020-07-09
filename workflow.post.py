import sys
import requests
import os
import json

url      = "https://api.github.com/repos/munderseth/my.dispatch/actions/workflows/wf.yml/dispatches"
GH_TOKEN  = os.getenv('GH_TOKEN')

headers = {
  'Content-Type': "application/json",
  'Accept': "application/vnd.github.v3+json",
  'Authorization': 'Token ' + GH_TOKEN,
}

inputs = {      
  "ref": "master",
  "p1": "testspace",
  "p2": "foo"
}

inputs2 = {      
  "ref": "master"
}

def main():
  global inputs

  payload = json.dumps(inputs2)
  print(payload)
  
  response = requests.request("POST", url, data=payload, headers=headers)
  print(response.status_code)

if __name__ == "__main__":  # pragma: no cover
    main()
