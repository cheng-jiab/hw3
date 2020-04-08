'''

client = pymongo.MongoClient('mongodb+srv://m220student:<password>@mflix-6auna.mongodb.net/test?retryWrites=true&w=majority')

'''
import tweepy
import pymongo
from random import sample

auth = tweepy.OAuthHandler('LwG8GPbodB36m4Bb6U5BKiggD', "3EiAJXuRDci8nnFmdLAhRgIqtAbezYAVEJpN7eVbIwKpmvB2am")
auth.set_access_token('1174542277630468096-3Wn6VBSMLOgV1Kcq0glxTBjirzQzG5', 'pmXdaGMos8LbWytFREMzOLNagAvNiEn38yTCWTJEBRPRx')

#client = pymongo.MongoClient('mongodb+srv://m220student:m220password@mflix-6auna.mongodb.net/test?retryWrites=true&w=majority')
client = pymongo.MongoClient('mongodb+srv://m220student:m220password@mflix-6auna.mongodb.net/test?retryWrites=true&w=majority')
hw03 = client.hw03
twi = hw03.twitter_1
hw03_1 = client.hw03
fri = hw03_1.friends_1
#api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
#user = api.get_user('twitter')
#print(user.screen_nane)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status)

class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = auth
        self.twitter_client = tweepy.API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self,num_tweets):
        tweets = []
        for tweet in tweepy.Cursor(self.twitter_client.user_timeline, id = self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self,num_friends):
        friend_list = []
        for friend in tweepy.Cursor(self.twitter_client.friends, id = self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
'''
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler('LwG8GPbodB36m4Bb6U5BKiggD', "3EiAJXuRDci8nnFmdLAhRgIqtAbezYAVEJpN7eVbIwKpmvB2am")
        auth.set_access_token('1174542277630468096-3Wn6VBSMLOgV1Kcq0glxTBjirzQzG5', 'pmXdaGMos8LbWytFREMzOLNagAvNiEn38yTCWTJEBRPRx')
        return auth
'''
if __name__ == '__main__':

#    myStreamListener = MyStreamListener()
#    myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
#    hash_tag = ['PUBG']

#   myStream.filter(track =hash_tag)
    screen_name = 'RockstarGames'
    final = []


    record = ['RockstarGames']
    for i in range(0,20):
        homearray = []
        friendarray = []
        dbarray = {}
        twitter_client = TwitterClient(screen_name)


        for i in twitter_client.get_user_timeline_tweets(10):
            home = {}
            print(i.entities['hashtags'])
            home['id'] = i.id
            home['created_at'] = i.created_at
            home['hashtags'] = i.entities['hashtags']
            home['text'] = i.text
            home['favorite_count'] = i.favorite_count
            home['retweet_count'] = i.retweet_count
            home['lang'] = i.lang
            home['source'] = i.source
            home['user'] = i.user.screen_name
            homearray.append(home)
        twi.insert_many(homearray)


        #print(twitter_client.get_user_timeline_tweets(20))
        max_followers = 0

        back_screen_name = []
        for user in twitter_client.get_friend_list(10):
            mongoDB = {}
            mongoDB['screen_name']= user.screen_name
            mongoDB['name'] = user.name
            mongoDB['description'] = user.description
            mongoDB['followers_count'] = user.followers_count
            mongoDB['friends_count'] = user.friends_count
            mongoDB['verified'] = user.verified
            friendarray.append(mongoDB)

            if user.followers_count > max_followers:
                screen_name = user.screen_name
                max_followers = user.followers_count

            if user.followers_count > 10000:
                back_screen_name.append(user.screen_name)


        fri.insert_many(friendarray)

        #if screen_name in record:
        back_up_name = str(sample(back_screen_name, 1)[0])
        screen_name = back_up_name

        record.append(screen_name)
        print(screen_name)


        #friendarray.append(home)
#        dbarray['homepage'] = homearray
#        dbarray['friends'] = friendarray
#        dbarray['max_follower_user'] = screen_name
#        final.append(dbarray)


        #screen_name = user.screen_name
        print(homearray,friendarray)
    #twi.insert_many(homearray)
    #fri.insert_many(friendarray)
    

    print('end')

