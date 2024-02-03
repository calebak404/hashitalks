import os
import requests
import json

team_token  = os.getenv("TEAM_TOKEN")

team_headers = {
                "Authorization": "Bearer " + team_token,
                "Content-Type": "application/vnd.api+json"
              }
base_url = "https://app.terraform.io/api/v2/"
organization_name = "hashitalks-demo"
workspace_name = "HCT-APP-LIB-D1"

# get workspace id
results = requests.get(base_url + "organizations/" + organization_name + "/workspaces?search[name]=" + workspace_name, headers=team_headers)
workspace_id= (results.json())["data"][0]["id"]
print("Workspace ID: " + workspace_id)

# create a configuration version
body = json.dumps({
    "data": {
        "type": "configuration-versions",
        "attributes": {
            "auto-queue-runs": False
        }
    }
})
results = requests.post(base_url + "workspaces/" + workspace_id + "/configuration-versions", headers=team_headers, data=body)
upload_url = (results.json())["data"]["attributes"]["upload-url"]
configuration_id = (results.json())["data"]["id"]

# upload configuration
config_file = open("./config/config.tar.gz", "rb")
upload_headers = {
    "Content-Type": "application/octet-stream"
}
results = requests.put(upload_url, headers=upload_headers, data=config_file)
if results.status_code == 200:
    print("Configuration uploaded")

# create a run
body = json.dumps({
    "data": {
        "type": "runs",
        "attributes": {
            "is-destroy": False,
            "message": "Hashcorps Demo API Run",
            "auto-apply": True
        },
        "relationships": {
            "workspace": {
                "data": {
                    "type": "workspaces",
                    "id": workspace_id
                }
            },
            "configuration-version": {
                "data": {
                    "type": "configuration-versions",
                    "id": configuration_id
                }
            }
        }
    }
})
results = requests.post(base_url + "runs", headers=team_headers, data=body)
if results.status_code == 201:
    print("Run created")
