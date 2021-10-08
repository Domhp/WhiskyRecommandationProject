import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle('files/redditReviewsCorrected.pkl')
ratings = pd.read_pickle('files/meanScores.pkl')
whisky_matrix = df.pivot_table(index = 'username', columns = 'Whisky Name', values = 'score')
sns.jointplot(x='score', y='count', data=ratings)

user_rating_HP12 = whisky_matrix['Ardbeg 10']
similar_to_HP12 = whisky_matrix.corrwith(user_rating_HP12)
corr_HP12 = pd.DataFrame(similar_to_HP12, columns=['correlation'])
corr_HP12.dropna(inplace=True)
corr_HP12_N = pd.merge(corr_HP12, ratings, left_on='Whisky Name', right_on='Whisky Name')
corr_HP12_N = corr_HP12_N[(corr_HP12_N['count'] > 10)].sort_values(by='correlation', ascending=False)
print(corr_HP12_N.head(10))

