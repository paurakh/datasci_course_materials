import sys
import json
import urllib
# import numpy

# creates a dictionary of word:mood
def getScores(afinnfile, scores):
    # print "Hi there"
    for line in afinnfile:
        # print type(line)
        term, score = line.split("\t")
        scores[term] = int(score)

# adds adds tweet dict in a variable
def getTweets(tweet_file, tweets):
    for line in tweet_file:
        try: 
            tweets.append(json.loads(line))
        except:
            pass


def main():

    # ########## get Scores from list given
    sent_file = open(sys.argv[1]) # setup files to open
    scores = {}
    getScores(sent_file, scores)

    # ######### get the tweets
    tweet_file = open(sys.argv[2])
    tweets = []
    getTweets(tweet_file, tweets)

    # ######### calculate mood score for each tweet
    tweets.pop(0) # the first one is field

    moodTweets = []
    for tweet in tweets:
        mood = 0
        if "text" in tweet:
            for word in tweet["text"].split():
                if word in scores: mood += scores[word]
        moodTweets.append(mood)

     
    print "Example tweet:"
    print "================="
    print tweets[-1]["text"]
    print "Mood Rating: ",  moodTweets[-1]
    print "================="

    print "Average tweet mood: ", float(sum(moodTweets))/float(len(moodTweets))

    
if __name__ == '__main__':
    main()




