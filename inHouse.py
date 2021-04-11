import requests
import random

players = int(input("How many players? "))
rerolls = int(input("How many rerolls? "))
mode = input("Assign champions per team or per player? ").lower()
print()

#pull ddragon version
ddragonVersion = requests.get(
                                "https://ddragon.leagueoflegends.com/realms/na.json").json()['dd']

#ask for list of champions based off of ddragonversion, then jsonify
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/"
                         + ddragonVersion + "/data/en_US/champion.json").json()

championPool = []

#add all champion names to list
for key in champions['data']:
    championPool.append(champions['data'][key]['name'])

    random.shuffle(championPool)


def perPerson():
    for player in range(0, players):
        print("Player " + str(player + 1))
        for reroll in range(0, rerolls):
            print('\t' + championPool.pop(0))
        print()


def perTeam():
    for team in range(0, 2):
        print("Team " + str(team + 1))
        for reroll in range(0, players * rerolls):
            print('\t' + championPool.pop(0))
        print()


if mode == "player":
    perPerson()
elif mode == "team":
    perTeam()
