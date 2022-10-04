import pandas as pd

df = pd.read_csv("atp_final.csv")


# this function returns the history of the matchs played between two players
def players_head2head(player1, player2, table):
    df_player = table[((table['first_player'] == player1) & (table['second_player'] == player2)) |
                      ((table['first_player'] == player2) & (table['second_player'] == player1))]

    return df_player


# this part is to calculate the cumulative winning for each player between them
first_player_list = [0, ]
second_player_list = [0, ]
for i in range(1, len(df)):
    first_player = df.loc[i]['first_player']
    second_player = df.loc[i]['second_player']

    df_players = players_head2head(first_player, second_player, df[0:i - 1])
    df_players = df_players.reset_index(drop=True)

    l = 0
    m = 0
    for i in range(len(df_players)):
        if df_players.loc[i]['first_player'] == first_player and df_players.loc[i]['winner_player'] == 1:
            l = l + 1
        elif df_players.loc[i]['second_player'] == first_player and df_players.loc[i]['winner_player'] == 2:
            l = l + 1
        elif df_players.loc[i]['first_player'] == second_player and df_players.loc[i]['winner_player'] == 1:
            m = m + 1
        elif df_players.loc[i]['second_player'] == second_player and df_players.loc[i]['winner_player'] == 2:
            m = m + 1
    first_player_list.append(l)
    second_player_list.append(m)

df['head_to_head'] = [a-b for a, b in zip(first_player_list, second_player_list)]

df.to_csv('atp_final.csv', index=False)
