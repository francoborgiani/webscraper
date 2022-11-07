import bs4
import requests
from config import config

class NewsPage():
  def __init__(self, news_site_uid, url):
    self._config = config()['news_sites'][news_site_uid] 
    self._queries = self._config['queries']
    self._html = None
    self.url = url

    self._visit(url)

  def _select(self, selector):
    return self._html.select(selector)

  def _visit(self, url):
    response = requests.get(url)

    response.raise_for_status()

    self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):
  def __init__(self, news_site_uid, url):
    super().__init__(news_site_uid, url)
 
  @property
  def article_links(self):
    links_list = []

    for link in self._select(self._queries['homepage_article_links']):
      if link and link.has_attr("href"):
        links_list.append(link)

    return set(link["href"] for link in links_list)

class ArticlePage(NewsPage):
  def __init__(self, news_site_uid, url):
    super().__init__(news_site_uid, url)
   
  @property
  def body(self):
    result = self._select(self._queries['article_body'])
    
    return result[0].text if len(result) else ''

  @property
  def title(self):
    result = self._select(self._queries['article_title'])
    
    return result[0].text if len(result) else ''