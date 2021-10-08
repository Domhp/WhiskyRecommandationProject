import pandas as pd

userRecords = pd.read_pickle('files/userRecords.pkl')
meanScores = pd.read_pickle('files/redditReviewsClust.pkl')
reviews = pd.read_pickle('files/redditReviews.pkl')

def pickWhiskyFromOne(whiskiesIn):
    minNoReviews = 5
    maxNoOfReviewUsed = 10
    dtPotentialWhisky = pd.DataFrame()
    for whiskyIn in whiskiesIn:
        dfTopReviews = meanScores.loc[meanScores['Whisky Name'] == whiskyIn, 'likedBy'].values[0]
        dfTopReviews = dfTopReviews[:maxNoOfReviewUsed]
        # Find the top whiskies top x people liked
        for name in dfTopReviews:
            temp = reviews.loc[(reviews['NumberOfReviews'] >= minNoReviews) & (reviews['username'] == name) & (
                        reviews['score'] - userRecords.loc[userRecords['username'] == name, 'distFromMean'].values[0] >= reviews['meanScore'])]
            dtPotentialWhisky = dtPotentialWhisky.append(temp)

    topList = dtPotentialWhisky['Whisky Name'].value_counts()
    print(topList.head(10))

if __name__ == "__main__":
    listOfWhiskies = ['Highland Park 12', 'Highland Park Einar', 'Laphroaig 10 Cask Strength']
    listOfWhiskiesTwo = ['Balvenie 12 Doublewood', 'Highland Park 12', 'Eagle Rare 10']
    pickWhiskyFromOne(listOfWhiskiesTwo)