from twython import Twython

APP_KEY = 'njGSEQU0f4s61U701IhKA'
APP_SECRET = 'mD5RCPLxrqTovGajgOMOX3Np98d6BonqgwsGX7uWfM'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

result = twitter.search(q='python')

#print(type(result))

#print(result.keys())

#print(result['statuses'])

search_results = twitter.search(q="python")

#print(search_results.keys())

for tweet in search_results["statuses"]:
    print ("Tweet from @%s Date: %s" % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
    print (tweet['text'].encode('utf-8'),"\n")
