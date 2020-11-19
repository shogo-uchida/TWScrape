# ツイートをエクセルファイルに出力する
import tweepy
import pandas as pd
import datetime

# TweepyAPI KEY
CONSUMER_KEY = 'V371ydaREQEXQlpGArWZ6e4k1'
CONSUMER_SECRET = '0kvuy5l07HKLn7NMhr2chn0XMYFrZUdzfohYWwpUK4sfBGkjfd'
ACCESS_TOKEN = '1032607424807546880-pNijjI3GUmimtbKfMvm0SxlhabDu0Q'
ACCESS_TOKEN_SECRET = '7Ty2uVVYPGlGQigp5DjT0k4vXqLPeWgAxmmfDgwItFxZm'
# tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
columns_name = ["TW_NO", "TW_TIME", "TW_TIME2", "TW_TEXT", "FAV", 'RT']
# ここで取得したいツイッターアカウントIDを指定する
tw_id = "cpfc_Japan"


# ツイート取得
def get_tweets():
    tweet_data = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tw_id, exclude_replies=True).items():
        tweet_data.append(
            [tweet.id, tweet.created_at, tweet.created_at + datetime.timedelta(hours=9), tweet.text.replace('\n', ''),
             tweet.favorite_count, tweet.retweet_count])
    df = pd.DataFrame(tweet_data, columns=columns_name)
    df.to_excel('tw_%s.xlsx' % tw_id, sheet_name='Sheet1')

    print("end")

get_tweets()