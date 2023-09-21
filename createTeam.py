import csv

team = [["File_Version", "2"]]
with open("team.txt", "r") as input:
    for index, line in enumerate(input):

        teamName = [
            "{:03}".format(index + 100), # Teams ID
            "", 
            "3", 
            line.strip(), #要在記分板上顯示的名稱
            "", 
            "", 
            "TWN"
        ]
        team.append(teamName)

print(team)

file_name = "teams.tsv"


with open(file_name, 'w', newline='') as teamsFile:
    writer = csv.writer(teamsFile, delimiter='\t')
    for row in team:
        writer.writerow(row)

print(f"{file_name} create sucess")
