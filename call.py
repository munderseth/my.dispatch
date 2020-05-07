import sys
import requests
import os
import json

url      = "https://api.github.com/repos/munderseth/my.dispatch/dispatches"
GH_TOKEN  = os.getenv('GH_TOKEN')

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.github.everest-preview+json",
     'Authorization': 'Token ' + GH_TOKEN,
  }

input = {      
  "event_type": "testspace1",
  "client_payload": {"function": "foo", "param1": "tbd"}
}

def main():
  global input

  payload = json.dumps(input)
  print(payload)
  
  response = requests.request("POST", url, data=payload, headers=headers)
  print(response.status_code)

if __name__ == "__main__":  # pragma: no cover
    main()
