import requests
import pandas as pd

from bs4 import BeautifulSoup

rank_list = []
player_list = []
value_list = []

response = requests.get("https://hoopshype.com/nba2k/2021-2022/")

if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("tr")
    for result in results:
        tr_column = result.select("td")
     
        rank = tr_column[0].text.strip()
        player_name = tr_column[1].text.strip()
        value = tr_column[2].text.strip()
        
        rank_list.append(rank)
        player_list.append(player_name)
        value_list.append(value)
    
nba_dict = {
    "rank": rank_list,
    "player_name": player_list,
    "value": value_list,
}

df = pd.DataFrame(nba_dict)

df.to_csv("NBA_2K22.csv")
