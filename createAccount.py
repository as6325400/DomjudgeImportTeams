import csv
import generator

team = [["accounts", "1"]]
with open("team.txt", "r") as input:
    for index, line in enumerate(input):
        # 這邊的19要先去看team的編號
        teamName = [
            "team", # 創建帳號的類型
            line.strip(), # user name
            "team" + "{:03}".format(index + 19), # 登陸用的帳號
            generator.generatorPassword(10) # 密碼，此處為隨機
        ]
        team.append(teamName)

print(team)

file_name = "accounts.tsv"


with open(file_name, 'w', newline='') as teamsFile:
    writer = csv.writer(teamsFile, delimiter='\t')
    for row in team:
        writer.writerow(row)

print(f"{file_name} create sucess")
