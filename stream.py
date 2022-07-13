import pandas as pd
import streamlit as st
from sklearn import ensemble, neighbors
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split


df2 = pd.read_csv("new_data_atp_2022.csv")
df1 = pd.read_csv("new_data_atp_2021.csv")

df = pd.concat([df1, df2], ignore_index=True)

df = df.dropna()
df = df[df.Wage != '(1']
df = df[df.Wheight != '0 c']
df = df[df.winner_weight != 'kg']
df = df[(df.winner_YTD_Titles != '2/1') & (df.winner_YTD_Titles != '0/1') & (df.winner_YTD_Titles != '0/2')
        & (df.winner_YTD_Titles != '1/3') & (df.winner_YTD_Titles != '0/0') & (df.winner_YTD_Titles != '2/4')
        & (df.winner_YTD_Titles != '9/14') & (df.winner_YTD_Titles != '1/1') & (df.winner_YTD_Titles != '7/14')
        & (df.winner_YTD_Titles != '4/6') & (df.winner_YTD_Titles != '3/5') & (df.winner_YTD_Titles != '2/5')]
df = df[df.Lage != '(1']
df = df[df.Lheight != '0 c']
df = df[df.loser_weight != 'kg']

df['winner_Career_Prize_Money'] = df['winner_Career_Prize_Money'].apply(lambda x: x.replace(',', '')).astype('float32')
df['loser_Career_Prize_Money'] = df['loser_Career_Prize_Money'].apply(lambda x: x.replace(',', '')).astype('float32')

df = df.replace(to_replace = ['$222,670', '$219,349', '$97,547', '$65,393', '$151,093', '$121,873', '$348,499',
                              '$82,650', '$100,085',
                              '$161,300', '$45,388', '$673,616', '$458,797', '$130,451', '$306,766', '$580,303', ','],
                value=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '.'])

df = df.reset_index(drop=True)

df = df.drop(['Winner', 'Loser', 'random_player'], axis=1)

df = df[0: len(df)-15]

st.title('tourney informations')

col1, col2, col3 = st.columns(3)

with col1:
    location = st.selectbox('tourney location', sorted(df['Tournament'].unique()))

with col2:
    court = st.selectbox('court', sorted(df['Court'].unique()))

with col3:
    surface = st.selectbox('surface', sorted(df['Surface'].unique()))


st.title('first player informations')

col1, col2, col3 = st.columns(3)

with col1:
    f_player_rank = st.number_input('first player rank')

with col1:
    f_player_age = st.number_input('first player age')

with col1:
    f_player_height = st.number_input('first player height')

with col1:
    f_player_weight = st.number_input('1st player weight')

with col2:
    f_player_hand = st.selectbox('1st player hand', ['R', 'L'])

with col2:
    f_player_ytd_w_L = st.number_input('1st player YTD Won-Lost')

with col2:
    f_player_ytd_titles = st.number_input('1st player YTD Titles')

with col2:
    f_player_winner_career = st.number_input('1st player winner CAREER W-L')

with col3:
    f_player_titles = st.number_input('first player titles')

with col3:
    f_player_career_prize = st.number_input('1st player Career Prize Money')

with col3:
    f_player_h2h = st.number_input('1st player h2h with 2nd player')


st.title('second player informations')

col1, col2, col3 = st.columns(3)

with col1:
    s_player_rank = st.number_input('second player rank')

with col1:
    s_player_age = st.number_input('second player age')

with col1:
    s_player_height = st.number_input('second player height')

with col1:
    s_player_weight = st.number_input('2nd player weight')

with col2:
    s_player_hand = st.selectbox('2nd player hand', ['R', 'L'])

with col2:
    s_player_ytd_w_L = st.number_input('2nd player YTD Won-Lost')

with col2:
    s_player_ytd_titles = st.number_input('2nd player YTD Titles')

with col2:
    s_player_winner_career = st.number_input('2nd player winner CAREER W-L')

with col3:
    s_player_titles = st.number_input('second player titles')

with col3:
    s_player_career_prize = st.number_input('2nd player Career Prize Money')

with col3:
    s_player_h2h = st.number_input('2nd player h2h with 1st player')


df.loc[len(df)] = [location, court, surface, f_player_rank, f_player_age, f_player_height, f_player_titles,
                   f_player_h2h, f_player_hand, f_player_weight, f_player_ytd_w_L, f_player_ytd_titles,
                   f_player_winner_career, f_player_career_prize, s_player_rank, s_player_age, s_player_height,
                   s_player_titles, s_player_h2h, s_player_hand, s_player_weight, s_player_ytd_w_L, s_player_ytd_titles,
                   s_player_winner_career, s_player_career_prize, 0]

if st.button('press to change the players'):
    df.loc[len(df)] = [location, court, surface, s_player_rank, s_player_age, s_player_height,
                       s_player_titles, s_player_h2h, s_player_hand, s_player_weight, s_player_ytd_w_L,
                       s_player_ytd_titles, s_player_winner_career, s_player_career_prize,
                       f_player_rank, f_player_age, f_player_height, f_player_titles,
                       f_player_h2h, f_player_hand, f_player_weight, f_player_ytd_w_L, f_player_ytd_titles,
                       f_player_winner_career, f_player_career_prize, 0]

else:
    df.loc[len(df)] = [location, court, surface, f_player_rank, f_player_age, f_player_height, f_player_titles,
                       f_player_h2h, f_player_hand, f_player_weight, f_player_ytd_w_L, f_player_ytd_titles,
                       f_player_winner_career, f_player_career_prize, s_player_rank, s_player_age, s_player_height,
                       s_player_titles, s_player_h2h, s_player_hand, s_player_weight, s_player_ytd_w_L,
                       s_player_ytd_titles, s_player_winner_career, s_player_career_prize, 1]

df[['Wrank', 'Wage', 'Wheight', 'Wtitles', 'Wh2h', 'winner_weight', 'winner_YTD_Won_Lost', 'winner_YTD_Titles',
    'winner_CAREER_W_L', 'winner_Career_Prize_Money', 'Lrank', 'Lage', 'Lheight', 'Ltitles', 'Lh2h', 'loser_weight',
    'loser_YTD_Won_Lost', 'loser_YTD_Titles', 'loser_CAREER_W_L', 'loser_Career_Prize_Money']] = \
    df[['Wrank', 'Wage', 'Wheight', 'Wtitles', 'Wh2h', 'winner_weight', 'winner_YTD_Won_Lost', 'winner_YTD_Titles',
        'winner_CAREER_W_L', 'winner_Career_Prize_Money', 'Lrank', 'Lage', 'Lheight', 'Ltitles', 'Lh2h', 'loser_weight',
        'loser_YTD_Won_Lost', 'loser_YTD_Titles', 'loser_CAREER_W_L', 'loser_Career_Prize_Money']].astype('float')

height_s = pd.cut(df['Wheight'], bins=[165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
df = df.join(pd.get_dummies(height_s, prefix='height_s'))


height_f = pd.cut(df['Lheight'], bins=[165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
df = df.join(pd.get_dummies(height_f, prefix='height_f'))


age_f = pd.cut(df['Wage'], bins=[15, 20, 25, 30, 35, 40, 45], labels=[1, 2, 3, 4, 5, 6])
df = df.join(pd.get_dummies(age_f, prefix='age_f'))


age_s = pd.cut(df['Lage'], bins=[15, 20, 25, 30, 35, 40, 45], labels=[1, 2, 3, 4, 5, 6])
df = df.join(pd.get_dummies(age_s, prefix='age_s'))


weight_w = pd.cut(df['winner_weight'], bins=[100, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 300],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
df = df.join(pd.get_dummies(weight_w, prefix='weight_w'))


weight_l = pd.cut(df['loser_weight'], bins=[100, 150, 160, 170, 180, 190, 200, 210, 220, 230, 300],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df = df.join(pd.get_dummies(weight_l, prefix='weight_l'))


career_w = pd.cut(df['winner_CAREER_W_L'], bins=[-500, -200, -100, 0, 100, 200, 300, 400, 500, 600, 2000],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df = df.join(pd.get_dummies(career_w, prefix='career_w'))


career_l = pd.cut(df['loser_CAREER_W_L'], bins=[-500, -200, -100, 0, 100, 200, 300, 400, 500, 600, 2000],
                  labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df = df.join(pd.get_dummies(career_l, prefix='career_l'))


prize_w = pd.cut(df['winner_Career_Prize_Money'],
                 bins=[0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000,
                       15000000, 20000000, 30000000, 50000000, 100000000, 1000000000],
                 labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
df = df.join(pd.get_dummies(prize_w, prefix='prize_w'))


prize_l = pd.cut(df['loser_Career_Prize_Money'],
                 bins=[0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000,
                       15000000, 20000000, 30000000, 50000000, 100000000, 1000000000],
                 labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
df = df.join(pd.get_dummies(prize_l, prefix='prize_l'))


df = df.drop(['Wheight', 'Lheight', 'Wage', 'Lage', 'winner_weight', 'loser_weight', 'winner_CAREER_W_L',
             'loser_CAREER_W_L', 'winner_Career_Prize_Money', 'loser_Career_Prize_Money'], axis=1)

df = df.reset_index(drop=True)

KNN = neighbors.KNeighborsClassifier(n_neighbors=5, metric='minkowski', weights='distance', p=2)
Decision_tree = DecisionTreeClassifier(criterion='entropy', max_depth=30)
Random_forest = ensemble.RandomForestClassifier(criterion='entropy', max_depth=30, n_estimators=150, n_jobs=-1)
clf_lr = LogisticRegression(max_iter=2000)

vclf = VotingClassifier(estimators=[('log_reg', clf_lr), ('knn', KNN), ('Decsion_tree', Decision_tree),
                                    ('random_forest', Random_forest)], voting='hard')

data = df.drop('winner_player', axis=1)
target = df['winner_player']

data = data.join(pd.get_dummies(data[['Tournament', 'Surface', 'Court', 'winner_hand', 'loser_hand']]))

data = data.drop(['Tournament', 'Surface', 'Court', 'winner_hand', 'loser_hand'], axis=1)

algo = vclf

# X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.2)

X_train = data[0:2167]
Y_train = target[0:2167]

X_test = data[2167:len(data)-1]
Y_test = target[2167:len(data)-1]

X_pred = data[len(data) - 1: len(data)]


algo.fit(X_train, Y_train)
algo_score = algo.score(X_test, Y_test)

algo_pred = algo.predict(X_pred)

if algo_pred[0] == 1:
    st.text('first player will win the match')
    st.write(algo_score)
if algo_pred[0] == 2:
    st.text('second player will win the match')
    st.write(algo_score)
