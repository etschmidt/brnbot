import requests
import random
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
auth = tweepy.OAuthHandler("R01stciClYF60ycRGvqrhwGsn", "0SzVv7JYuljAYiojQ3pHNaUHhgdYNQjdua5JivT8UxLSiYYJ4R")
auth.set_access_token("1072002479137669123-BCgOEnZJVWS2G5etIFZ6lpg3Y5Cv7C", "4xXvcI3n5hhIdfahq9R2SGqapJYBbRMi50spgC4t3BIRp")

api = tweepy.API(auth)

api.update_status("From the archives:\n\n" + title + " " + link)