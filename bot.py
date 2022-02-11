import praw;

reddit = praw.Reddit(
   client_id="_zPAk6W7c3SoKuMBFnuwkg",
   client_secret="GHK0hQVMmK3l5Xia0ibRONclREh74A",
   password="adityaq@1",
   user_agent="testscript by u/adiBest333",
   username="adiBest333",
)
print(reddit.user.me())
print("Hello world")
print(reddit.user.me())
subreddits=['SelfPromotionYouTube','YouTubeviews']

Title="Zayn mallik best song ever"
Link="https://www.youtube.com/watch?v=AY9blLYMKnI"

for subreddit in subreddits:
    reddit.subreddit(subreddit).submit(Title,url=Link,send_replies=False)

