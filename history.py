import requests
import json
import time
import pandas as pd

from bs4 import BeautifulSoup
from team import return_player_list

months = ["october", "november", "december", "january", "february", "march" , "april", "may", "june"]
# months = ["october", "november"]

team1_list=[]
score1_list=[]
team2_list=[]
score2_list=[]
winner_list=[]
home_list=[]
players1_list=[]
players2_list=[]


with open("team.json", "r") as json_file:
    name_dict = json.load(json_file)


for month in months:
    response=requests.get(f"https://www.basketball-reference.com/leagues/NBA_2022_games-{month}.html")

    if response.ok:
        soup=BeautifulSoup(response.text,"html.parser")
        results=soup.find_all("tr")
        flag = 0
        for result in results:
            if flag == 0:
                flag = flag+1
                continue

            tr_row=result.select("td")

            team1 = tr_row[1].text.strip()
            score1 = tr_row[2].text.strip()
            team2 = tr_row[3].text.strip()
            score2 = tr_row[4].text.strip()

            team1_player = return_player_list(name_dict[team1])
            team2_player = return_player_list(name_dict[team2])
            print(f"{team1} : {team1_player}")
            print("\n")
            print(f"{team2} : {team2_player}")
            if score1>score2:
                winner=team1
            else:
                winner=team2
            home=team2

            team1_list.append(team1)
            score1_list.append(score1)
            team2_list.append(team2)
            score2_list.append(score2)
            winner_list.append(winner)
            home_list.append(home)
            players1_list.append(team1_player)
            players2_list.append(team2_player)
            time.sleep(5)

nba_dict={
    "team1": team1_list,
    "score1": score1_list,
    "team2": team2_list,
    "score2": score2_list,
    "winner": winner_list,
    "home": home_list,
    "players1": players1_list,
    "players2": players2_list,
}

df = pd.DataFrame(nba_dict)
df.to_csv("NBA_2022_Season.csv") 
        
        
