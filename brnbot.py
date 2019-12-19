import requests
import random
import os
from bs4 import BeautifulSoup

URL = 'https://www.boredroomnews.com/general'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# get all the card links from General archive

cards = soup.find_all('a', class_="text-dark", )

# randomize choice

card = random.choice(cards)
print(card)

title = card.text
link = card.attrs['href']

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

api.update_status("From the archives:\n\n" + title + " " + link)