import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = '/home/admin1/Desktop/PythonVM/NLPProblems/tweet_data.txt'
data = pd.read_csv('/home/admin1/Desktop/PythonVM/NLPProblems/tweet_data.txt')
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


print(tweets_data)
