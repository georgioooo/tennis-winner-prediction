import pandas as pd
import numpy as np

df = pd.read_csv('atp_final.csv')


# History table of each player By Surface
def surface_player(player, surface, table):
    df_player = table[(table['first_player'] == player) & (table['surface'] == surface) |
                      (table['second_player'] == player) & (table['surface'] == surface)]

    return df_player


player1_AceAverage_surface = [0]

# This part is for calculate the Ace average history by surface for the first player
for i in range(1, len(df)):

    player1 = df.loc[i]['first_player']
    player1_surface = df.loc[i]['surface']
    df_player1 = surface_player(player1, player1_surface, df[0:i - 1])
    df_player1 = df_player1.reset_index(drop=True)

    ace_number = 0  # number of aces
    if len(df_player1) > 0:
        for j in range(len(df_player1)):
            if df_player1.loc[j]['first_player'] == player1:
                ace_number = ace_number + df_player1.loc[j]['first_player_ace']

            elif df_player1.loc[j]['second_player'] == player1:
                ace_number = ace_number + df_player1.loc[j]['second_player_ace']

        player1_AceAverage_surface.append(round(ace_number / len(df_player1), 1))

    else:
        player1_AceAverage_surface.append(np.nan)

df['player1_AceAverage_surface'] = player1_AceAverage_surface

player2_AceAverage_surface = [0]
# This script is for calculate the Ace average history by surface for the second player
for i in range(1, len(df)):
    player2 = df.loc[i]['second_player']
    player2_surface = df.loc[i]['surface']

    df_player2 = surface_player(player2, player2_surface, df[0:i - 1])
    df_player2 = df_player2.reset_index(drop=True)

    ace_number = 0
    if len(df_player2) > 0:
        for j in range(len(df_player2)):
            if df_player2.loc[j]['first_player'] == player2:
                ace_number = ace_number + df_player2.loc[j]['first_player_ace']

            elif df_player2.loc[j]['second_player'] == player2:
                ace_number = ace_number + df_player2.loc[j]['second_player_ace']

        player2_AceAverage_surface.append(round(ace_number / len(df_player2), 1))

    else:
        player2_AceAverage_surface.append(np.nan)

df['player2_AceAverage_surface'] = player2_AceAverage_surface

df.to_csv('atp_final.csv', index=False)
