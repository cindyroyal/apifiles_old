#
# Tasks
#    - insert key and access tokens
#    - complete loop for fetching multiple sets of results 
# 


import oauth2 as oauth        # oauth authorization needed for twitter API
import json, re               # converting data into json object, using replace 
from pprint import pprint     # pretty print 


# function to construct url for search query 
# max_id is set to 0 if only two arguments are passed 
def makeurl(searchterm, count, max_id=0) :
    baseurl = "https://api.twitter.com/1.1/search/tweets.json"
    if max_id == 0:
        url = baseurl + '?q=' + searchterm + '&' \
              + 'count=' + count    
    else:
        url = baseurl + '?q=' + searchterm + '&' \
              + 'max_id=' + str(max_id) + '&' \
              + 'count=' + count    
    return url 


#request input from the command line, must import re for the substitutions
my_raw_searchterm = raw_input(' * What are your search terms? ')
my_searchterm = re.sub(r'#','%23', my_raw_searchterm)
searchTermShort = re.sub(r'#', '', my_raw_searchterm)
searchTermShort = re.sub(r' ', '', searchTermShort)

# determine loop count 
MAX_RESULTS_FROM_TWITTER = 100
desired_max_count = input(' * How many tweets do you want? ')


url = makeurl(my_searchterm, str(MAX_RESULTS_FROM_TWITTER))

# my keys, need all four of them. Use your own keys here.
consumer_key = "USE YOUR CREDENTIALS"
consumer_secret = "USE YOUR CREDENTIALS"
token_key = "USE YOUR CREDENTIALS"
token_secret = "USE YOUR CREDENTIALS"

# set up oauth tokens
token = oauth.Token(token_key, token_secret)
consumer = oauth.Consumer(consumer_key, consumer_secret)

# create client and request data 
client = oauth.Client(consumer, token)



loopcount = desired_max_count / MAX_RESULTS_FROM_TWITTER 


# -------------------------------
# complete loop code below  
# -------------------------------

for i in range(loopcount):
# loop to pull results 100 at a time 

    # fetch search results 
    header,contents = client.request(url, method="GET")
    

    # convert results to json object 
    data = json.loads(contents)

    # write retrieved data to a unique file based on i
    # will overwrite files of same name
    filename = searchTermShort + str(i) + '.json'
    localfile = open(filename, 'w');
    localfile.write(contents);
     

    # find number of search results 
    results = len(data['statuses'])

    # find the oldest tweet
    next_id = data['statuses'][results-1]['id']
    

    # get date for oldest tweet and print
    oldest_tweet_date = data['statuses'][results-1]['created_at']
    print(oldest_tweet_date)
    

    # construct search query to fetch tweets older than the current tweet 
    url = makeurl(my_searchterm, str(MAX_RESULTS_FROM_TWITTER), next_id)





