from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import pymongo
import json
from bson.json_util import dumps


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, timeout, stream,hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(timeout,stream,hash_tag_list)
        auth = OAuthHandler('LwG8GPbodB36m4Bb6U5BKiggD', "3EiAJXuRDci8nnFmdLAhRgIqtAbezYAVEJpN7eVbIwKpmvB2am")
        auth.set_access_token('1174542277630468096-3Wn6VBSMLOgV1Kcq0glxTBjirzQzG5', 'pmXdaGMos8LbWytFREMzOLNagAvNiEn38yTCWTJEBRPRx')
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, timeout,stream,hash_tag_list):
        self.timeout= timeout
        self.fetched_tweets_filename=stream
        self.hash_tag_list = hash_tag_list

    def on_data(self, data):
        try:
            print(data)
            '''
            with open(self.fetched_tweets_filename, 'a') as tf:
                data = str({'hashtag': self.hash_tag_list, 'data': data})
                tf.write(data)
            '''
            #data = str(data[1:-1])
            data = json.loads(data)
            self.fetched_tweets_filename.insert_one(data)

            if time.time() > timeout:
                print('Times up!')
                return False
            else:

                return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.

    client = pymongo.MongoClient(
        'mongodb+srv://m220student:m220password@mflix-6auna.mongodb.net/test?retryWrites=true&w=majority')
    hw03 = client.hw03
    game = hw03.game
    stream = hw03.stream
    game =game.distinct('name')

    timeout = time.time() + 60 * 10
    hash_tag_list = []
    for i in game:

        hash_tag_list.append(i)
        #fetched_tweets_filename = "tweets.txt"
        print(i)

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(timeout,stream,hash_tag_list)


