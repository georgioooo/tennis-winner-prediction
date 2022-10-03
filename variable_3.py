import pandas as pd
import numpy as np

df = pd.read_csv('atp_final.csv')


# History table of each player By Surface
def player_history_by_surface(player, surface, table):
    df_player = table[((table['first_player'] == player) & (table['surface'] == surface)) |
                      ((table['second_player'] == player) & (table['surface'] == surface))]

    return df_player


# This part is for calculate the average winning history by surface for the first player
player1_win_prob_surface_alltime = [0]
for i in range(1, len(df)):
    player1 = df.loc[i]['first_player']
    player1_surface = df.loc[i]['surface']

    df_player1 = player_history_by_surface(player1, player1_surface, df[0:i - 1])
    df_player1 = df_player1.reset_index(drop=True)

    l = 0
    m = 0
    if len(df_player1) > 0:
        for i in range(len(df_player1)):
            if df_player1.loc[i]['first_player'] == player1 and df_player1.loc[i]['winner_player'] == 1:
                l = l + 1
            elif df_player1.loc[i]['second_player'] == player1 and df_player1.loc[i]['winner_player'] == 2:
                l = l + 1
            elif df_player1.loc[i]['first_player'] == player1 and df_player1.loc[i]['winner_player'] == 2:
                m = m + 1
            elif df_player1.loc[i]['second_player'] == player1 and df_player1.loc[i]['winner_player'] == 1:
                m = m + 1
        player1_win_prob_surface_alltime.append(round(l / len(df_player1), 3))

    else:
        player1_win_prob_surface_alltime.append(np.nan)
