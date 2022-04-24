import csv
from termcolor import colored
from pyfiglet import  figlet_format
import random

f = open('CoronaTweetsWithinLastMinute.csv')
csv_f = csv.reader(f)

tweets = []

for row in csv_f:
    tweets.append(row[10])

def text_art(str):
    result = figlet_format(str)
    #color = input("Pick a color to display tweet (blue, green, cyan, grey, magenta): ")
    valid_colors= ("blue", "cyan", "green", "grey", "magenta")
    
    #if color not in valid_colors:
     #   return colored(result, color= "magenta")
    #else:
    for i in valid_colors:
        color = random.choice(valid_colors)
        return colored(result, color)

donaldTrumpTweets = set(tweets)
for i in donaldTrumpTweets:
    print(text_art(i))