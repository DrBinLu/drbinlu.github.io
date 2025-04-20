import tweepy
import os

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

screen_name = "DrBinLu"
tweet_count = 3
tweets = api.user_timeline(screen_name=screen_name, count=tweet_count, tweet_mode="extended", exclude_replies=True, include_rts=False)

with open("tweets.md", "w", encoding="utf-8") as f:
    f.write("## 🐦 Recent on X\n\n")
    for tweet in tweets:
        url = f"https://x.com/{screen_name}/status/{tweet.id}"
        text = tweet.full_text.replace("\n", " ").strip()
        f.write(f"- [{text}]({url})\n")
