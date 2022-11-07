from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError
import news_objects
import logging
from datetime import datetime
import csv

logger = logging.getLogger()

def fetch(news_site_uid, link):
  logger.info(f"Start fetching article at {link}") 
  
  article = None
  
  try:
    article = news_objects.ArticlePage(news_site_uid=news_site_uid, url=link)
  except (HTTPError, MaxRetryError) as e:
    logger.warning("Error while fetching the article", exc_info=False)
  
  if article and not article.body:
    logger.warning("Error, the article don't have a body")
    return None
  
  if article and not article.title:
    logger.warning("Error, the article don't have a title")
    return None
  
  return article

def save_all(articles, news_site_uid):
  date_now = datetime.now().strftime('%Y_%m_%d')
  out_filename = f"{news_site_uid}_{date_now}_articles.csv"
  
  csv_header = list(
    filter(lambda property: not property.startswith("_"), dir(articles[0]))
  )

  with open(out_filename, mode="w+") as f:
    writer = csv.writer(f)
    
    writer.writerow(csv_header)
    
    for article in articles:
      writer.writerow(str(getattr(article, prop)) for prop in csv_header)
      
  logger.info(f"Articles was written on {out_filename}")