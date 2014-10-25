import json                   # converting data into json object 
from pprint import pprint     # pretty print 
import string                 # extracting filename
import sys                    # command-line arguments


if len(sys.argv) != 2 : 
    print("usage : ")
    print("\t python tweet_geo.py filename")
    sys.exit()


# grab json file
filename = sys.argv[1]

# construct output csv filename from json file
# if json file is foo.json then csv file is foo.csv
splitname = string.split(filename, '.')
fields = len(splitname)

ext = splitname[fields - 1]
name = splitname[0]

csvfilename = name + ".csv"
csvfile = open(csvfilename, 'a');


# open file and load data 
localfile = open(filename, 'r');
data = json.load(localfile)

# get number of tweets in file 
tweets = len(data['statuses'])

for i in range(tweets):
    # text of the tweet 
    tweet_text = data['statuses'][i]['text']
    
    # date tweet was sent 
    date = data['statuses'][i]['created_at']

    # full name of user 
    name = data['statuses'][i]['user']['name']
    
    # username (without the @)
    username = data['statuses'][i]['user']['screen_name']
    
    # combine and create CSV text 
    csv_text = name + ","  + username + "," + date + "," + "\"" + tweet_text + "\"" + "\n"

    # dump to file 
    csvfile.write(csv_text.encode('utf8'))
