import pandas as pd
import numpy as np

df = pd.read_csv('atp_final.csv')


# History table of each player By Surface
def player_history_by_surface(player, surface, table):
    df_player = table[((table['first_player'] == player) & (table['surface'] == surface)) |
                      ((table['second_player'] == player) & (table['surface'] == surface))]

    return df_player


# This part is for calculate the average winning history by surface for the first player
player1_win_avr_surface_alltime = [0]
for i in range(1, len(df)):
    player1 = df.loc[i]['first_player']
    player1_surface = df.loc[i]['surface']

    df_player1 = player_history_by_surface(player1, player1_surface, df[0:i - 1])
    df_player1 = df_player1.reset_index(drop=True)

    winning_cumulation = 0
    if len(df_player1) > 0:
        for j in range(len(df_player1)):
            if df_player1.loc[j]['first_player'] == player1 and df_player1.loc[j]['winner_player'] == 1:
                winning_cumulation = winning_cumulation + 1
            elif df_player1.loc[j]['second_player'] == player1 and df_player1.loc[j]['winner_player'] == 2:
                winning_cumulation = winning_cumulation + 1
        player1_win_avr_surface_alltime.append(round(winning_cumulation / len(df_player1), 3))

    else:
        player1_win_avr_surface_alltime.append(np.nan)

df['player1_win_avr_surface_alltime'] = player1_win_avr_surface_alltime

# This part is for calculate the average winning history by surface for the second player
player2_win_avr_surface_alltime = [0]
for i in range(1, len(df)):
    player2 = df.loc[i]['second_player']
    player2_surface = df.loc[i]['surface']

    df_player2 = player_history_by_surface(player2, player2_surface, df[0:i - 1])
    df_player2 = df_player2.reset_index(drop=True)

    winning_cumulation = 0
    if len(df_player2) > 0:
        for j in range(len(df_player2)):
            if df_player2.loc[j]['first_player'] == player2 and df_player2.loc[j]['winner_player'] == 1:
                winning_cumulation = winning_cumulation + 1
            elif df_player2.loc[j]['second_player'] == player2 and df_player2.loc[j]['winner_player'] == 2:
                winning_cumulation = winning_cumulation + 1
        player2_win_avr_surface_alltime.append(round(winning_cumulation / len(df_player2), 3))

    else:
        player2_win_avr_surface_alltime.append(np.nan)

df['player2_win_avr_surface_alltime'] = player2_win_avr_surface_alltime

df.to_csv('atp_final.csv', index=False)
