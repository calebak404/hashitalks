import os
import requests
import json

user_token = os.getenv("USER_TOKEN")
team_token = os.getenv("TEAM_TOKEN")
org_token  = os.getenv("ORG_TOKEN")

user_headers = {
                "Authorization": "Bearer " + user_token,
                "Content-Type": "application/vnd.api+json"
              }

team_headers = {
                "Authorization": "Bearer " + team_token,
                "Content-Type": "application/vnd.api+json"
              }

org_headers = {
                "Authorization": "Bearer " + org_token,
                "Content-Type": "application/vnd.api+json"
              }

# Get the current user
user_response = requests.get("https://app.terraform.io/api/v2/account/details", headers=user_headers)
team_response = requests.get("https://app.terraform.io/api/v2/account/details", headers=team_headers)
org_response = requests.get("https://app.terraform.io/api/v2/account/details", headers=org_headers)

print(json.dumps(user_response.json(), indent = 2))
print(json.dumps(team_response.json(), indent = 2))
print(json.dumps(org_response.json(), indent = 2))
