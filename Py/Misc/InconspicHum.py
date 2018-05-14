

import praw, random

bot = praw.Reddit(user_agent='InconspicuousHuman',
                  client_id='h14_mF9hf1LIfQ',
                  client_secret='VauL7z5IQG6J7yBSxa2F2eM8Vpc',
                  username='InconspicuousHuman',
                  password='IMadeThisForYouButNotReallyWhenItIsGivenMakeIt')



StrToFind = "every account on reddit is a bot except you."

PossibleMessages = ["and also me...", "and inconspicuous humans...", "Well at least I'm not a bot...", "Every bot on reddit is you.", "Every account on reddit is a bot, including you.", "I forgot I was supposed to say."]

subreddit = bot.subreddit('awesomebots')

comments = subreddit.stream.comments()

AlreadyRepliedComments = []

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if comment not in AlreadyRepliedComments:
	    if StrToFind in text.lower():
	        # Generate a message
	        message = random.choice(PossibleMessages)
	        comment.reply(message) # Send message
	        AlreadyRepliedComments.append(comment)