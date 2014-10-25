# 
# Tasks 
#    - insert own key and access token 
#    - use a different search term 
#    - rename saved file 
#    - add one more search criteria
#        look at https://dev.twitter.com/rest/reference/get/search/tweets for options
#

import oauth2 as oauth        # oauth authorization needed for twitter API
import json                   # converting data into json object 
from pprint import pprint     # pretty print 
    

# construc search url
# baseurl is the twitter api
# use %23 to represent hashtag symbol
# count is 100, twitter default without using a loop to get more
# play with changing the search term
# I added searchTermShort to concatenate in filename. See below.

baseurl = "https://api.twitter.com/1.1/search/tweets.json"
searchterm = "%23mcweek"
searchTermShort = "mcweek"
count = "100"

# the url we are using includes baseurl plus ?q to open query plus search term, adding & and count
url = baseurl + '?q=' + searchterm + '&' + 'count=' + count

# my keys, need all four of them. Use your own keys here.
consumer_key = "USE YOUR CREDENTIALS"
consumer_secret = "USE YOUR CREDENTIALS"
token_key = "USE YOUR CREDENTIALS"
token_secret = "USE YOUR CREDENTIALS"

# set up oauth tokens
token = oauth.Token(token_key, token_secret)
consumer = oauth.Consumer(consumer_key, consumer_secret)

# create client and request data from url
client = oauth.Client(consumer, token)
header, contents = client.request(url, method="GET")

# write retrieved data to file 
# concatenate searchTermShort in filename
filename = searchTermShort + '_tweets.json'
localfile = open(filename, 'w');
localfile.write(contents);

# convert to json object 
data = json.loads(contents)

# print meta data on search results 
pprint(data['search_metadata'])



