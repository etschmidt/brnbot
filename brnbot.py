import requests
import random
import tweepy
from os import environ
from bs4 import BeautifulSoup

URL = 'https://www.boredroomnews.com/general'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# get all the card links from General archive
cards = soup.find_all('a', class_="text-dark", )

# randomize choice
card = random.choice(cards)

title = card.text
link = card.attrs['href']

print(title + " " + link)

# post_page = requests.get(link)
# soup = BeautifulSoup(post_page.content, 'html.parser')

# image = soup.find("img",  {"class": "featured-image"})
# image_src = image.attrs['src'] + "?" + str(random.random())

# print(image_src)

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

api.update_status("From the archives:\n\n" + title + " " + link)