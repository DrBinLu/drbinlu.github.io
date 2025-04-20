import os
import tweepy

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

user = client.get_user(username="DrBinLu").data
tweets = client.get_users_tweets(id=user.id, max_results=5, tweet_fields=["text", "created_at"])

with open("tweets.md", "w", encoding="utf-8") as f:
    f.write("## 🐦 Recent on X\n\n")
    if not tweets.data:
        f.write("*No recent tweets found.*\n")
    else:
        for tweet in tweets.data:
            tweet_url = f"https://x.com/DrBinLu/status/{tweet.id}"
            text = tweet.text.replace("\n", " ").strip()
            f.write(f"- [{text}]({tweet_url})\n")
