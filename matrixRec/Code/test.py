import pandas as pd
import numpy as np

reviews = pd.read_pickle('files/redditReviews.pkl')
ratings = pd.read_pickle('files/meanScores.pkl')
userRecords = pd.read_pickle('files/userRecords.pkl')

minNoReviews = 4
maxNoOfReviewUsed = 10
userLikedList = []
for whiskyName in ratings['Whisky Name']:

    meanScore = ratings.loc[ratings['Whisky Name'] == whiskyName, 'score'].values[0]
    whiskyInReviews = reviews.loc[reviews['Whisky Name'] == whiskyName]

    # Find the top x people who liked whiskyIn
    dfTopReviews = pd.DataFrame()
    for r in whiskyInReviews.iloc:
        if (r['score'] - userRecords.loc[userRecords['username'] == r['username'], 'distFromMean'].values[0] >= meanScore):
            if (userRecords.loc[userRecords['username'] == r['username'], 'reviewCount'].values[0] >= minNoReviews):
                dfTopReviews = dfTopReviews.append(r, ignore_index=True)
    # Refine list top 5 Reviewers
    tempList = []
    if(dfTopReviews.empty == False):
        dfTopReviews.sort_values(by=['score'], inplace=True, ignore_index=True, ascending=False)
        dfTopReviews = dfTopReviews.iloc[:maxNoOfReviewUsed]
        tempList = dfTopReviews['username'].tolist()
    userLikedList.append(tempList)
print(userLikedList)

print(len(ratings))
print(len(userLikedList))
ratings['likedBy'] = userLikedList
ratings.to_pickle('files/redditReviewsClust.pkl')
ratings.to_csv('files/redditReviewsClust.csv')