#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3697073121-KSe24vq1P0qmKxSUpiIsmvlPTcfTnZwgUeJQPhM"
access_token_secret = "QRUK9BeNR6ogN0NZ3aci8IjG5tuANN00mLy4yNlQI5sqV"
consumer_key = "ql8w8iqe43L9Piwvqt5XNVlGs"
consumer_secret = "7OOFMgoWSFMUS8bMW9KerFHoq5neA1zDZ8qHB0moR6lvC2vFvy"
           
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Apple', 'Google', 'Microsoft', 'Facebook', 'Oracle', 'iPhone', 'iPad', 'iPod', 'Macbook'])