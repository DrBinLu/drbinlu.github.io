import feedparser

FEED_URL = "https://nitter.poast.org/DrBinLu/rss"
OUTPUT_PATH = "tweets.md"
NUM_TWEETS = 3

print(f"Fetching feed from: {FEED_URL}")
feed = feedparser.parse(FEED_URL)

if not feed.entries:
    print("❌ No entries found in feed.")
    with open(OUTPUT_PATH, "w") as f:
        f.write("## 🐦 Recent on X\n\n")
        f.write("*Unable to fetch tweets right now.*\n")
        f.write(f"[Try opening the feed manually]({FEED_URL})\n")
    exit(0)

print(f"✅ Retrieved {len(feed.entries)} entries.")
with open(OUTPUT_PATH, "w") as f:
    f.write("## 🐦 Recent on X\n\n")
    for entry in feed.entries[:NUM_TWEETS]:
        title = entry.title.replace("\n", " ").strip()
        link = entry.link
        f.write(f"- [{title}]({link})\n")
