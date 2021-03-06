import collections
import itertools
import json
import os
from collections import Counter

from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# define variables
articles_path = []
articleTitles = []
articleData = []
articleCount = 0
reliableArticleCount = 0
unreliableArticleCount = 0

#  a list of all sources for the articles in the NELA2017 dataset
sources = ["AP", "BBC", "Business Insider", "CBS News", "CNBC", "CNN", "Counter Current News",
           "Daily Buzz Live", "MotherJones", "National Review", "NPR", "PBS", "Salon", "Slate",
           "Talking Points Memo", "The Atlantic", "The Fiscal Times", "The Guardian", "The Hill",
           "The New York Times", "Vox", "Xinhua", "Activist Post", "Addicting Info", "Alternative Media Syndicate",
           "Bipartisan Report", "Breitbart", "BuzzFeed", "Conservative Tribune", "Daily Kos",
           "Daily Mail", "Daily Stormer", "DC Gazette", "Drudge Report", "End the Fed", "Faking News",
           "Fox News", "Freedom Daily", "Freedom Outpost", "FrontPage Magazine", "Fusion", "Hang The Bankers",
           "Infowars", "Intellihub", "Investors Business Daily", "Liberty Writers", "National Report", "Natural News",
           "New York Daily News", "New York Post", "NewsBusters", "Newslo", "NODISINFO", "Observer",
           "Occupy Democrats", "Palmer Report", "Prntly", "Raw Story", "Real News Right Now", "RedState",
           "RT", "Shareblue", "The Beaverton", "The Chaser", "The D.C. Clothesline", "The Duran",
           "The Gateway Pundit", "The Huffington Post", "The Right Scoop", "The Shovel", "The Spoof",
           "TheBlaze", "ThinkProgress", "True Pundit", "TruthFeed", "USA Politics Now", "USA Today",
           "Veterans Today", "Washington Examiner", "World News Politics", "Yahoo News"]

#  a sublist of the sources that have been deemed reliable after research
reliableSources = ["AP", "BBC", "Business Insider", "CBS News", "CNBC", "CNN", "Counter Current News",
                   "Daily Buzz Live", "MotherJones", "National Review", "NPR", "PBS", "Salon", "Slate",
                   "Talking Points Memo", "The Atlantic", "The Fiscal Times", "The Guardian", "The Hill",
                   "The New York Times", "Vox", "Xinhua"]

#  a sublist of the sources that have been deemed unreliable after research
unreliableSources = ["Activist Post", "Addicting Info", "Alternative Media Syndicate", "Bipartisan Report", "Breitbart",
                     "BuzzFeed", "Conservative Tribune", "Daily Kos", "Daily Mail", "Daily Stormer",
                     "DC Gazette", "Drudge Report", "End the Fed", "Faking News", "Fox News", "Freedom Daily",
                     "Freedom Outpost", "FrontPage Magazine", "Fusion", "Hang The Bankers", "Infowars", "Intellihub",
                     "Investors Business Daily", "Liberty Writers", "National Report", "Natural News",
                     "New York Daily News", "New York Post", "NewsBusters", "Newslo", "NODISINFO", "Observer",
                     "Occupy Democrats", "Palmer Report", "Prntly", "Raw Story", "Real News Right Now", "RedState",
                     "RT", "Shareblue", "The Beaverton", "The Chaser", "The D.C. Clothesline", "The Duran",
                     "The Gateway Pundit", "The Huffington Post", "The Right Scoop", "The Shovel", "The Spoof",
                     "TheBlaze", "ThinkProgress", "True Pundit", "TruthFeed", "USA Politics Now", "USA Today",
                     "Veterans Today", "Washington Examiner", "World News Politics", "Yahoo News"]

#  listdir() returns a list containing the names of the entries in the directory path given
# ['1_April', '2_May', '3_June', '4_July', '5_August', '6_September', '7_October'] is returned from NELA2017
month_directories = os.listdir("C:/NELA2017/NELA2017.tar/NELA2017")


#  need an object to hold the month and date info together
class Directories:
    def __init__(self, month, date):
        self.month = month
        self.date = date


for m in month_directories:  # go through all items in month_directories and get contents
    #  date_directories in the form ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04', '2017-10-05'.....]
    date_directories = os.listdir("C:/NELA2017/NELA2017.tar/NELA2017/" + m)
    # create a list of objects that hold both the month and date for article paths
    directoryPath = Directories(m, date_directories)
    articles_path.append(directoryPath)

#  the path to the files with the HTML is C:/NELA2017/NELA2017.tar/NELA2017/"month"/"date"/"source"/"article_title.txt"
for s in sources:
    articleCount = 0
    for p in articles_path:
        for d in p.date:
            fileFound = True
            try:
                #  get a list of articleTitles for that source on that date in format
                #  ['AP--2017-04-17--Absences fitness atmosphere _ new ways to track schools.txt',.....]
                articleTitles = os.listdir("C:/NELA2017/NELA2017.tar/NELA2017/" + p.month + "/" + d + "/" + s)
            except FileNotFoundError:
                fileFound = False

            if fileFound:  # if the source had articles on that date open all articles using articleTitles list
                for articleTitle in articleTitles:
                    if articleTitle != "PaxHeader":
                        # open the file and specify mode (read, write, etc.)
                        # using the keyword "with automatically closes the file afterwards
                        with open("C:/NELA2017/NELA2017.tar/NELA2017/" + p.month + "/" + d + "/" + s + "/" +
                                  articleTitle, 'rb') as file:
                            try:
                                # count number of articles in each source
                                articleCount = articleCount + 1
                            except ValueError:
                                print("JsonDecodeError for file " + articleTitle)

    print(s)
    print(articleCount)

    if s in reliableSources:
        reliableArticleCount = reliableArticleCount + articleCount
    elif s in unreliableSources:
        unreliableArticleCount = unreliableArticleCount + articleCount
print("reliable sources number of articles: " + str(reliableArticleCount))
print("unreliable sources number of articles: " + str(unreliableArticleCount))
