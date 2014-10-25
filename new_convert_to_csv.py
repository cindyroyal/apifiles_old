import json                   # converting data into json object 
from pprint import pprint     # pretty print 
import string                 # extracting filename
import sys                    # command-line arguments
import os                     # os functions


if len(sys.argv) != 2 : 
    print("usage : ")
    print("\t python tweet_geo.py filename")
    sys.exit()
    
# include number of files you are converting
# this will work for up to 100 files. Change numfile if you have more
numfile = 100;    

#goes through each file starting with 0 in filename 
for j in range(numfile):
	# grab base filename from command line
	filename = sys.argv[1]
	

	# construct output csv filename from json file
	# if json file is foo.json then csv file is foo.csv
	splitname = string.split(filename, '.')
	fields = len(splitname)

	ext = splitname[fields - 1]
	
	#adds j to csv name to create separate file for each
	name = splitname[0] + str(j)
    
    # checks to see if file exists before proceeding
	if os.path.isfile(name + '.json'):
		csvfilename = name + ".csv"
		csvfile = open(csvfilename, 'w');

	
		# open file and load data, uses csv name to open each file, starting with 0
		localfile = open(name + '.json', 'r');
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
