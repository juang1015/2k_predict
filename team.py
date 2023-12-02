import requests
import pandas as pd

from bs4 import BeautifulSoup


def return_player_list(team):
    response=requests.get(f"https://www.basketball-reference.com/teams/{team}/2022.html")

    name_list=[]
    if response.ok:
        soup=BeautifulSoup(response.text,"html.parser")
        results=soup.find_all("tr")
        for result in results:
            th_row = result.select("th")
            if th_row[0]["data-stat"] == "number":
                tr_row=result.select("td")   
                if len(tr_row)==0:
                    continue
                name = tr_row[0].text.strip()
                name_list.append(name)
        
        return name_list

