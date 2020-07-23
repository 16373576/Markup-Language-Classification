import os
import json
from collections import Counter
from nltk.tokenize import word_tokenize

htmlData = []
tokenHtml = []
articleTitles = os.listdir("C:/gossipcop/fakehtml/")
for title in articleTitles:
    if not os.path.isfile("C:/gossipcop/fakehtmlfreq/" + title + ".txt"):
        try:
            with open("C:/gossipcop/fakehtml/" + title, 'rb') as file:
                articleData = []
                tokenHtml.clear()
                articleData = json.load(file)
                tokenHtml = word_tokenize(articleData)
                previousToken = " "
                for token in tokenHtml:
                    if len(token) > 1 and token[0] == "/" and token[1] != "/" and previousToken == "<":
                        htmlData.append(token)
                    previousToken = token
        except FileNotFoundError:
            print("file not found")
        if len(htmlData) != 0:
            with open("C:/gossipcop/fakehtmlfreq/" + title + ".txt", 'a') as newFile:
                newFile.write(str(Counter(htmlData)) + "\n")
            htmlData.clear()
            print(title + " tags counted and added to file")
