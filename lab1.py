import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

import nltk 
from nltk.corpus import twitter_samples 
import random

nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print('Total positive tweets: ', len(all_positive_tweets))
print('Total negative tweets: ', len(all_negative_tweets))
print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
print('The type of a tweet entry is: ', type(all_negative_tweets[0]))