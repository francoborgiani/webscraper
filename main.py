import argparse
import logging
logging.basicConfig(level=logging.INFO)

from config import config
import news_objects

logger = logging.getLogger()

def main(news_site_uid):
  host = config()['news_sites'][news_site_uid]['url']
  
  logger.info(f"Beginning scraper for url {host}")
  
  news_object = news_objects.NewsPage(news_site_uid, host)

if __name__ == "__main__":
  # Instance arg parser
  parser = argparse.ArgumentParser()

  #  Get News Sites Choices from the config
  news_sites_choices = list(config()['news_sites'].keys())

  # Request Arguments in the prompt
  parser.add_argument('news_site_uid',
                      help="The news site that you want to scrap",
                      choices=news_sites_choices,
                      type=str)

  # Get parsed arguments
  args = parser.parse_args() 
  
  main(args.news_site_uid)