import json

#http://files.pushshift.io/reddit/comments/
json_file = open('RC_2011-07')
data = json.load(json_file)

#parse
#I am thinking grab the subreddit and comment
#subreddit will be true groups
#clusters should match subreddits
#Processing....