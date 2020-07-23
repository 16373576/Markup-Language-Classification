from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import TooManyRedirects
import pandas as pd
import os
import json

# df = pd.read_csv("C:/gossipcop/gossipcop_fake.csv", header=0, delimiter=",")
df = pd.read_csv("C:/gossipcop/gossipcop_real.csv", header=0, delimiter=",")
urls = df["news_url"]
titles = df["title"]
index = 0

for URL in urls:
    number = len(titles)
    if index <= number:
        title = titles[index]
        title = title.replace("?", "")
        title = title.replace("/", "")
        title = title.replace(":", "")
        title = title.replace("*", "")
        title = title.replace('"', "")
        title = title.replace("|", "")
        index = index + 1
    if not os.path.isfile("C:/gossipcop/realhtml/" + title + ".txt"):
   # if not os.path.isfile("C:/gossipcop/fakehtml/" + title + ".txt"):
        print(title)
        try:
            content = requests.get(URL)
            soup = BeautifulSoup(content.text, 'html.parser')
            soupString = str(soup)
            with open("C:/gossipcop/realhtml/" + title + ".txt", 'w') as newFile:
            # with open("C:/gossipcop/fakehtml/" + title + ".txt", 'w') as newFile:
                json.dump(soupString, newFile)
        except ConnectionError as e:
            print("\n connection error, file skipped " + title)
        except TooManyRedirects as p:
            print("\n too many redirects, file skipped " + title)
