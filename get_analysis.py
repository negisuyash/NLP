
import tweepy

from textblob import TextBlob




consumer_token='___________GET YOUR OWN CONSUMER TOKEN_________________'
consumer_secret='___________SECRET TO KEEP,CANT SHARE______________'



access_token='___________GET YOUR OWN ACCESS TOKEN_________________'
access_token_secret='___________SECRET TO KEEP,CANT SHARE______________'


auth=tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token,access_token_secret)



api=tweepy.API(auth)

print("Enter the keyword you want to search")
topic=input()


public_post=api.search(topic)

sad=0
happy=0
#not_sure=0

for tweet in public_post:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	senti=analysis.sentiment.polarity
	print(senti)
	if(senti<0):
	    sad=sad+1
	if(senti>0):
	    happy=happy+1
	#if(senti==0):
	#    not_sure=not_sure+1

#print(str(sad)+" "+str(happy)+"  "+str(not_sure)+" ")
if(sad>=happy):
    print("\nPeople are sad.")
else:
    print("\n People are happy.")

