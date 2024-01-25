import tweepy
from pymongo import MongoClient
from fastapi import FastAPI
import uvicorn

client = MongoClient('mongodb://dio:dio@localhost:27017/')

db = client.my_test

tweets_collection = db.tweets

tweets_collection.insert_one{{'author':'teste', 'text':'Abracadabra'}}

tweets = tweets_collection.find({})

print(list(tweets))

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends', response_model=List[TrendItem])
def get_trends_route():
    trends = get_trends(woe_id=BRAZIL_WOE_ID)
    return trends

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=8000)

