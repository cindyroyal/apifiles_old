
#---UPDATES-------------------------------------------------
# - Swapped sys_arg for pythonic input. (accepts hashtags)
# - Concatenated output: date,user,tweet - now in .csv
# - Cleaned-up the console output.
#-----------------------------------------------------------

import oauth2 as oauth
import json, sys, re
import time, csv


#PROMPT SEARCH TERMS / VOLUME
print ' TWEET FETCH (RESTING API)'
print ' ================================='
searchTerm = raw_input(' * What are your search terms? ')
searchTerm = re.sub(r'#',"%23", searchTerm)
desired_max_count = input(' * How many tweets do you want? ')


#COUNT CYCLES
MAX_RESULTS_FROM_TWITTER = 100
loopcount = desired_max_count / MAX_RESULTS_FROM_TWITTER


#NOTIFY USER, PAUSE
print '\n ---------------------------------'
print ' * ' + str(loopcount) + ' SETS IN FETCH QUEUE'
print ' * STARTING IN (2) SECONDS.'
time.sleep(2)


#CREATE THE URL
def makeurl(searchterm, max_id=0) :
    baseurl = "https://api.twitter.com/1.1/search/tweets.json"
    count = "100"
    if max_id == 0:
        url = baseurl + '?q=' + searchterm + '&' \
              + 'count=' + count    
    else:
        url = baseurl + '?q=' + searchterm + '&' \
              + 'max_id=' + str(max_id) + '&' \
              + 'count=' + count    
    return url 
url = makeurl(searchTerm)


# my keys, need all four of them. Use your own keys here.
consumer_key = "vOtsK3aCJWd0zKwofLDaCQ"
consumer_secret = "LxVohFyoF3sFhve4FL6ZoNLMs7dQUd9g2cs7NLuk"
token_key = "1246761-39k6SCDVPLh8yIzuzRDZCVzX2Sukll6e2gPyz3zNEB"
token_secret = "MpO6F1Mb4VmD3mGsbsevepSKp3gI9VfCTigbMyz2oArcy"



# OAUTH / CLIENT AUTH
token = oauth.Token(token_key, token_secret)
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer, token)


# LOOP CONTENT INTO OUTPUT
localfile = open('output.csv','w')
print '\n ---------------------------------'
for i in range(loopcount):
    header, contents = client.request(url, method="GET")
    data = json.loads(contents)
    print ' * FETCH #' + str(i+1) + ' | SUCCESS!'
    results = len(data['statuses'])  
    
    for j in range(results):
        tweet= data['statuses'][j]['text']
        date = data['statuses'][j]['created_at']
        user = data['statuses'][j]['user']['screen_name']

        tweet = re.sub(r'\n',"", tweet) #PURGE ERRENOUS NEWLINES
        tweet = re.sub(r'\n\n',"", tweet)
        
        tweet= tweet.encode('ascii', 'ignore')
        date = date.encode('ascii', 'ignore')
        user = user.encode('ascii', 'ignore')

        localfile.write(date+',@'+user+','+tweet+'\n');

    if results < 100:
        break

    next_id = data['statuses'][results - 1]['id']
    url = makeurl(searchTerm, next_id)

localfile.close()
print '\n ================================='
print ' OUTPUT WRITE COMPLETE'
