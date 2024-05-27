import requests
from bs4 import BeautifulSoup
import math
from datetime import datetime
import random

class News:
    def __init__(self, text: str, link: str, time: str, category: str):
        self.text = text
        self.link = link
        self.time = time
        self.category = category

class NewsService:
    def __init__(self):
        self.base_url = f'https://lenta.ru'

    def get_news_day(self, quantity=1, year='2024', month='01', day='01'):
        """format @year @mont @day: 0000 00 00"""
        page_limit = math.ceil(quantity / 30) + 1
        news = []
        for page in range(1, page_limit):
            url = f'{self.base_url}/{year}/{month}/{day}/page/{page}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Парсинг цитат
            news_html_list = soup.find_all('li', class_='archive-page__item _news')
            for news_html in news_html_list:
                text = news_html.find('h3').text.strip()
                link = self.base_url + news_html.find('a').get('href')
                time = news_html.find('time').text.strip()
                category = news_html.find('span').text.strip()

                new = News(text, link, time, category)
                news.append(new)
        return news[:quantity]
    
    def get_news_day_by_category(self, quantity=1, year='2024', month='01', day='01', category = None):
        """
        format @year @mont @day: 0000 00 00
        @category: russia, world, ussr, economics, forces, science, sport, culture, media, style, travel, life, realty, wellness
        """
        categories = ['russia', 'world', 'ussr', 'economics', 'forces', 'science', 'sport', 'culture', 'media', 'style', 'travel', 'life', 'realty', 'wellness']
        if category not in categories:
            return []
        page_limit = math.ceil(quantity / 30) + 1
        news = []
        for page in range(1, page_limit):
            url = f'{self.base_url}/rubrics/{category}/{year}/{month}/{day}/page/{page}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Парсинг цитат
            news_html_list = soup.find_all('li', class_='archive-page__item _news')
            for news_html in news_html_list:
                text = news_html.find('h3').text.strip()
                link = self.base_url + news_html.find('a').get('href')
                time = news_html.find('time').text.strip()
                category = news_html.find('span').text.strip()

                new = News(text, link, time, category)
                news.append(new)
        return news[:quantity]

    def get_new_news(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d")
        page_limit = 25
        for page in range(page_limit, 1 , -1):
            url = f'{self.base_url}/{current_datetime[:4]}/{current_datetime[5:7]}/{current_datetime[8:10]}/page/{page}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Парсинг цитат
            news_html_list = soup.find_all('li', class_='archive-page__item _news')
            for news_html in news_html_list:
                text = news_html.find('h3').text.strip()
                link = self.base_url + news_html.find('a').get('href')
                time = news_html.find('time').text.strip()
                category = news_html.find('span').text.strip()
                new = News(text, link, time, category)
                return new

    def get_random_news(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d")
        page_limit = 25
        news = []
        for page in range(1, page_limit):
            url = f'{self.base_url}/{current_datetime[:4]}/{current_datetime[5:7]}/{current_datetime[8:10]}/page/{page}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Парсинг цитат
            news_html_list = soup.find_all('li', class_='archive-page__item _news')
            for news_html in news_html_list:
                text = news_html.find('h3').text.strip()
                link = self.base_url + news_html.find('a').get('href')
                time = news_html.find('time').text.strip()
                category = news_html.find('span').text.strip()

                new = News(text, link, time, category)
                news.append(new)
        return random.choice(news)