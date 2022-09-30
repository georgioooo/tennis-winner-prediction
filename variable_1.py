import pandas as pd
import numpy as np

df = pd.read_csv('df.csv')


# History table of a player
def player_history(player, table):
    df_player = table[(table['first_player'] == player) | (table['second_player'] == player)]

    return df_player


player1_AceAverage_AllTime = [0]

# This script is for calculate the Ace average history of the first player
for i in range(1, len(df)):

    player1 = df.loc[i]['first_player']
    df_player1 = player_history(player1, df[0:i - 1])
    df_player1 = df_player1.reset_index(drop=True)

    ace_number = 0
    if len(df_player1) > 0:
        for j in range(len(df_player1)):
            if df_player1.loc[j]['first_player'] == player1:
                ace_number = ace_number + df_player1.loc[j]['first_player_ace']

            elif df_player1.loc[j]['second_player'] == player1:
                ace_number = ace_number + df_player1.loc[j]['second_player_ace']

        player1_AceAverage_AllTime.append(round(ace_number / len(df_player1), 1))

    else:
        player1_AceAverage_AllTime.append(np.nan)

df['player1_AceAverage_AllTime'] = player1_AceAverage_AllTime


# This script is for calculate the Ace average history for the second player
player2_AceAverage_AllTime = [0]

for i in range(1, len(df)):

    player2 = df.loc[i]['second_player']
    df_player2 = player_history(player2, df[0:i - 1])
    df_player2 = df_player2.reset_index(drop=True)

    ace_number = 0
    if len(df_player2) > 0:
        for j in range(len(df_player2)):
            if df_player2.loc[j]['first_player'] == player2:
                ace_number = ace_number + df_player2.loc[j]['first_player_ace']

            elif df_player2.loc[j]['second_player'] == player2:
                ace_number = ace_number + df_player2.loc[j]['second_player_ace']

        player2_AceAverage_AllTime.append(round(ace_number / len(df_player2), 1))

    else:
        player2_AceAverage_AllTime.append(np.nan)

df['player2_AceAverage_AllTime'] = player2_AceAverage_AllTime

df.to_csv('atp_final.csv', index=False)