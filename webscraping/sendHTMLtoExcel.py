import json
import os
import numpy as np
import ast


def main():
    # initialize variables
    listOfDictionaryValues = []
    articleTitles = os.listdir("C:/gossipcop/realhtmlfreq/")

    # get list of all tags
    listOfTags = get_list_of_all_tags()

    # sort the dictionaries
    sort_tags(listOfTags, articleTitles)

    # create a numpy array to send to csv file
    listOfDictionaryValues.append(str(list(listOfTags)))
    for title in articleTitles:
        with open("C:/gossipcop/realhtmlsorted/" + title) as file:
            for cnt, line in enumerate(file):
                line = line.replace("Counter(", "").replace(")", "")
                lineDict = eval(line)
                listOfDictionaryValues.append(str(list(lineDict.values())) + title)
    listForExcel = np.hstack(listOfDictionaryValues)
    np.savetxt("C:/gossipcop/Realexcel.csv", listForExcel, delimiter="\n", fmt='%s', encoding="utf-8")


def get_list_of_all_tags():
    listOfAllTags = []

    # get a list of all tags
    with open("C:/gossipcop/listOfAllTags" + ".txt") as file:
        listOfAllTags = file.read()
        listOfAllTags = ast.literal_eval(listOfAllTags)
    return listOfAllTags


def sort_tags(list_of_tags, titles):
    for title in titles:
        if not os.path.isfile("C:/gossipcop/realhtmlsorted/" + title):
            dictKey = {}
            sortedArticles = []
            print(title)
            with open("C:/gossipcop/realhtmlfreq/" + title) as file:
                for cnt, line in enumerate(file):
                    line = line.replace("Counter(", "").replace(")", "")
                    print("Line {}: {}".format(cnt, line))
                    if not line:
                        continue
                    lineDict = eval(line)

                    # update the dict of each article in source with 0 if a tag from the list of all tags isn't in dict
                    for tag in list_of_tags:
                        if tag not in lineDict:
                            dictKey = {tag: 0}
                            lineDict.update(dictKey)

                    # reorder the dictionaries to match the order of the list of all tags
                    sortedDict = {}
                    sortedDict.clear()
                    for tag in list_of_tags:
                        getDictValues = {tag: lineDict[tag]}
                        sortedDict.update(getDictValues)
                    with open("C:/gossipcop/realhtmlsorted/" + title, 'a') as newFile:
                        newFile.write(str(sortedDict) + "\n")


main()
