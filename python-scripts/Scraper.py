import random
# import Classifier

from MemeScraper import RedditScraper
import database_interface

scraper = RedditScraper()
subreddits = ['ProgrammerHumor', 'wholesomememes']
subreddits = ['ProgrammerHumor']
for subreddit in subreddits:
    result = scraper.scrape_subreddit(subreddit, 200)
    for item in result:
        item['dankness'] = int(item['ups'] / 1000)
        item['spiciness'] = int(item['num_comments'] / 10)
        database_interface.upload_train_meme(item)
        # print(item)
