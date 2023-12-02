import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

value_df = pd.read_csv("NBA_2K23.csv")

player_value_dict = {}
for idx,row in value_df.iterrows():
    player_name = row["player_name"]
    player_value = row["value"]

    player_name = player_name.replace(" ", "")

    player_value_dict[player_name] = player_value

input = []
output = []

player_df = pd.read_csv("NBA_2023_Season_new.csv")
# print(player_df)
for idx,row in player_df.iterrows():
    team1_2k_value = 0
    team2_2k_value = 0

    team1 = row["team1"]
    team2 = row["team2"]
    home = row["home"]
    winner = row["winner"]

    if home == team1:
        home_team1 = 1
        home_team2 = 0
    else:
        home_team1 = 0
        home_team2 = 1

    if winner == team1:
        winner_team1 = 1
        winner_team2 = 0
    else:
        winner_team1 = 0
        winner_team2 = 1

    players_1 = row["players1"]
    players_2 = row["players2"]

    players_1 = eval(players_1.replace(" ", ""))
    players_2 = eval(players_2.replace(" ", ""))

    value_1 = []
    value_2 = []
    for player1 in players_1:
        if player1 in player_value_dict:
            value_1.append(int(player_value_dict[player1]))
        else:
            value_1.append(60)

    for player2 in players_2:
        if player2 in player_value_dict:
            value_2.append(int(player_value_dict[player2]))
        else:
            value_2.append(60)

    value_1 = sorted(value_1, reverse=True)
    value_1 = sorted(value_1, reverse=True)

    team1_2k_value = 0
    team2_2k_value = 0
    for idx in range(12):
        team1_2k_value = team1_2k_value + value_1[idx]
        team2_2k_value = team2_2k_value + value_2[idx]

    team1_avg_value = team1_2k_value / 12.0
    team2_avg_value = team2_2k_value / 12.0
    
    team1_feature = [team1_avg_value, home_team1]
    team1_result = winner_team1

    input.append(team1_feature)
    output.append(team1_result)

    team2_feature = [team2_avg_value, home_team2]
    team2_result = winner_team2

    input.append(team2_feature)
    output.append(team2_result)

X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.2, random_state=42)

logisticModel = LogisticRegression(random_state=0)

logisticModel.fit(X_train, y_train)

print(f"訓練得分 : {logisticModel.score(X_train, y_train)}")
print(f"測試得分 : {logisticModel.score(X_test, y_test)}")