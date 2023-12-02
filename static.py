import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

players = players.get_players()
player_ids = []
for player in players:
    id = player["id"]
    full_name = player["full_name"]

    player_ids.append([id, full_name])

df = pd.DataFrame()

for player in player_ids:
    id = player[0]
    full_name = player[1]

    career = playercareerstats.PlayerCareerStats(player_id=id)

    career_df = career.get_data_frames()[0]
    career_df = career_df[["PLAYER_ID", "SEASON_ID", "GP", "MIN"]]

    career_df["MP"] = (career_df["MIN"] / career_df["GP"]).astype(float).round(2)

    career_df["SEASON_ID"] = career_df["SEASON_ID"].apply(
        lambda x: "20" + x.split("-")[-1] if x[0] == "2" else "19" + x.split("-")[-1]
    )

    df = pd.concat([df, career_df], axis=0)

    print(f"Player : {full_name} has been processed!")

print(df)