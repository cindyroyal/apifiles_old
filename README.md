apifiles
========

Files associated with API assignment

This repository includes several Python files to use for basic scraping of the Twitter API. 

tweet_basic.py - this is the basic scraping file; it pulls contents of Twitter API for a designated search term in the file for the API limit. Created by Apan Qasem

tweet_mult_py - this script uses a loop to go through the API for multiple passes to get more than the 100 tweet limit. It will pull 100 tweets, then go to the oldest tweet and start another search from there. I have modified so that it accepts multiple search terms, hashtags, right on the command line. And you are prompted for the number of tweets. This results in multiple json files, one for each pass. Each file is created with a unique name based on the iteration through the loop. Imports re for replacement functions. The JSON files this creates includes all contents from Twitter API that are relevan to search terms.  Created by Apan Qasem, modified by Cindy Royal. . 


new_convert_json_to_csv.py - This file is modified from the one that Apan Qasem created. It goes through every json file in a folder and converts each to csv - grabbing text, created_at date, name and screen_name. These fields can be modified. This will create a series of csv files. If you want to concatenate all the csv files to one, it's easy to do on command line cat *.csv >combined.csv. I added the loop to go through each file in the folder and to replace hashtag and spaces in filenames for the output files. numfile variable holds the max files it will search for, but you can increase if you have more than 100. Script will end if it gets to an iteration of the filename and a file does not exist. Had to import os at top of script. 

Once you have the combined.csv, you can easily open in Excel and start anaylizing the data.

There are example files to illustrate output for searches for #mcweek AND journalism.

Play with these files for your own searches. This is a good way to start working with data to see if there are interesting trends or stories in the data set.
