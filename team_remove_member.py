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


# Remove a team member
team_member_email = "caleb.s@gmail.com"

# get team id
results = requests.get(base_url + "organizations/" + organization_name + "/teams?include=users&q=" + team_name, headers=org_headers)
team_id = (results.json())["data"][0]["id"]

#get user id
results = requests.get(base_url + "organizations/" + organization_name + "/organization-memberships", headers=org_headers)
user_id = [ user for user in (results.json())["data"] if user["attributes"]["email"] == team_member_email][0]["id"]

# add user to team
body = json.dumps({
    "data": [
        {
            "type": "organization-memberships",
            "id": user_id
        }
    ]
})

results = requests.delete(base_url + "teams/" + team_id + "/relationships/organization-memberships", headers=org_headers, data=body)
if results.status_code == 204:
    print("User " + team_member_email + " removed from team " + team_name)
else:
    print("Error adding user to team: " + str(results.json()))
