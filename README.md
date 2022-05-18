# tweetprofanitycheck
this project checks the degree of profanity of tweets in a given file
ASSUMPTIONS:
1) Tweet data is in english
2) I have taken a single csv file of choice containing tweets
3) racial , slur and white I have assumed as the given profain words for calculating degree of profanity

Procedure followed
1)loaded the csv file
2)removed duplicated and dropped null columns
3) preprocess the data by lowering characters, removing mentions ,hashtags,punctuations,any pattern and then tokezing the tweets
4) formula used for calculating degree of profanity= (total number of profain words in the tweet/total words in the tweet)*100
5) After this I have sorted the data frame in descending order with respect to column degreeofprofanity.
