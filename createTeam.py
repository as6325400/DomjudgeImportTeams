import json

team = []  # Start with a dictionary for the file version

with open("team.txt", "r") as input:
    for name, idx in enumerate(input):
        team_data = {
            "id": "{:03}".format(idx + 100),  # Team ID
            "group_ids": ["participants"],
            "name": name,  # Name to display on the scoreboard
            "organization_id": "utrecht",  # Organization ID
        }
        team.append(team_data)

print(team)

file_name = "teams.json"

# Write the data to a JSON file
with open(file_name, 'w') as teamsFile:
    json.dump(team, teamsFile, indent=4)

print(f"{file_name} created successfully")
