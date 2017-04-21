from MemeScraper import RedditScraper
import database_interface

scraper = RedditScraper()
result = scraper.scrape_subreddit("wholesomememes", 20)
for item in result:
    database_interface.upload_train_meme(item)
    print(item)
