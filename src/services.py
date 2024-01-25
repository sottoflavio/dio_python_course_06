import tweepy
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

def get_trends(woe_id: int) -> List[Dict[Literal, Any]]:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    for tweet in trends:
        print(tweet)

    return [trend for trend in trends]
