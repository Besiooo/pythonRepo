import requests
import string
from bs4 import BeautifulSoup


def spaces_to_underscores(word):
    word = [ch if ch != ' ' else '_' for ch in word]
    return ''.join(word)


def remove_punctuation(word):
    exclude = set(string.punctuation)
    exclude.add('’')
    return ''.join(ch for ch in word if ch not in exclude)


def format_names(word):
    word = remove_punctuation(word)
    word = spaces_to_underscores(word)
    return word


def comprehense_soup_finder(tags, attrs, to_find):
    if to_find == "href":
        return [x.get(to_find) for x in tags.find_all("a", attrs)]
    return [x.text for x in tags.find_all(to_find, attrs)]


class Scraper:
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    connection = None
    correct_code = 200
    articles_names = []
    articles_data = []
    soup = None
    article_req = "News"

    def connect(self):
        self.connection = requests.get(self.url)
        return self.connection.status_code

    def gather_data(self):
        self.soup = BeautifulSoup(self.connection.content, "html.parser")
        a_attrs = {"data-track-action": "view article"}
        span_attrs = {"class": "c-meta__type"}
        article_types = comprehense_soup_finder(self.soup, span_attrs, "span")
        article_titles = comprehense_soup_finder(self.soup, a_attrs, "a")
        article_hrefs = comprehense_soup_finder(self.soup, a_attrs, "href")
        self.articles_data = [[article_types[i], article_titles[i], article_hrefs[i]] \
                              for i in range(len(article_types))]
        print(self.articles_data)

    def filter_data(self):
        self.articles_data = [x for x in self.articles_data if x[0] == self.article_req]
        print(self.articles_data)

    def get_articles_names(self):
        self.articles_names = [format_names(x[1]) \
                               for x in self.articles_data]

    def save_file(self):
        for article in self.articles_data:
            i = self.articles_data.index(article)
            with open(f"{self.articles_names[i]}.txt", "wb") as file:
                print(f"Saving...{i + 1}/3")
                article_url = "https://www.nature.com" + article[2]
                article_connect = requests.get(article_url)
                article_soup = BeautifulSoup(article_connect.content, "html.parser")
                article_soup = article_soup.find("body")
                file.write(bytes(article_soup.text, encoding="utf-8"))
                print(f"Saved! {i + 1}/3")

    def __init__(self):
        if self.connect() == self.correct_code:
            self.gather_data()
            self.filter_data()
            self.get_articles_names()
            self.save_file()


Scraper()
