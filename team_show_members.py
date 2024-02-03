import os
import requests
import json

org_token  = os.getenv("ORG_TOKEN")

org_headers = {
                "Authorization": "Bearer " + org_token,
                "Content-Type": "application/vnd.api+json"
              }
base_url = "https://app.terraform.io/api/v2/"
organization_name = "hashitalks-demo"
team_name = "hct-team-lib-d1"

# Get team id and show members
results = requests.get(base_url + "organizations/" + organization_name + "/teams?include=users&q=" + team_name, headers=org_headers)
team_id = (results.json())["data"][0]["id"]
team_members = [ member["id"] for member in (results.json())["data"][0]["relationships"]["users"]["data"] ]
print("Team ID: " + team_id)
print("Team Members: " + ','.join(team_members))
