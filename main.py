import praw, json, sys, datetime
from time import sleep

with open("config.txt") as config_file:
    config_json = json.load(config_file)
    userAgent = config_json['userAgent']
    cID = config_json['cID']
    cSC = config_json['cSC']
    userN = config_json['userN']
    userP = config_json['userP']

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('askminecraft')
target_subreddit = reddit.subreddit('minecrafthelp')

while True:
    try:
        start_time = datetime.datetime.now()
        for submission in subreddit.stream.submissions():
            submission_time = datetime.datetime.fromtimestamp(submission.created_utc)
            if submission_time > start_time:
                submission.crosspost(target_subreddit, title='[X-Post] ' + submission.title)

    except:
        # Some error was thrown - sleep a minute
        print(sys.exc_info())
        sleep(60)
