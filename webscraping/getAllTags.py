import os
import json

articleTitles1 = os.listdir("C:/gossipcop/fakehtmlfreq/")
articleTitles2 = os.listdir("C:/gossipcop/realhtmlfreq/")
listOfAllTags = []

for title in articleTitles1:
    with open("C:/gossipcop/fakehtmlfreq/" + title) as file:
        for cnt, line in enumerate(file):
            line = line.replace("Counter(", "").replace(")", "")
            print("Line {}: {}".format(cnt, line))
            if not line:
                continue
            unreliableTags = eval(line)
    for unreliableKey in unreliableTags.keys():
        if unreliableKey not in listOfAllTags:
            listOfAllTags.append(unreliableKey)

for title in articleTitles2:
    with open("C:/gossipcop/realhtmlfreq/" + title) as file2:
        for cnt, line in enumerate(file2):
            line = line.replace("Counter(", "").replace(")", "")
            print("Line {}: {}".format(cnt, line))
            if not line:
                continue
            reliableTags = eval(line)
    for reliableKey in reliableTags.keys():
        if reliableKey not in listOfAllTags:
            listOfAllTags.append(reliableKey)

with open("C:/gossipcop/listOfAllTags.txt", 'a') as newFile:
    newFile.write(str(listOfAllTags))
