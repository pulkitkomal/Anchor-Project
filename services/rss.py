import feedparser


class RSS():
    """This is used to fetch RSS feeds.
    """
    def __init__(self, number_of_summaries=10) -> None:
        self.newsfeed = feedparser.parse("https://www.livemint.com/rss/technology")
        self.number_of_summaries = number_of_summaries
        
    def get_summaries(self):
        entry = self.newsfeed.entries[:self.number_of_summaries]
        summaries = [_['summary'] for _ in entry]
        return summaries