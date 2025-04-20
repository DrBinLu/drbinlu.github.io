import feedparser

FEED_URL = "https://nitter.net/DrBinLu/rss"
OUTPUT_PATH = "tweets.md"
NUM_TWEETS = 3

feed = feedparser.parse(FEED_URL)

if not feed.entries:
    with open(OUTPUT_PATH, "w") as f:
        f.write("## 🐦 Recent on X\n\n*Unable to fetch tweets right now.*\n")
    exit()

with open(OUTPUT_PATH, "w") as f:
    f.write("## 🐦 Recent on X\n\n")
    for entry in feed.entries[:NUM_TWEETS]:
        link = entry.link
        title = entry.title.replace("\n", " ").strip()
        f.write(f"- [{title}]({link})\n")
