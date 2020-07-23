# Markup-Language-Classification
### Using markup language to differentiate between reliable and unreliable news 

This repository contains the code used to extract HTML tags from articles and the code used run the classification algorithms which used the HTML tags as attributes.
The code is divided up into 4 directories:


###### 1. Classification:

This directory contains 3 python scripts, one which will produce the results for 10-fold cross validation, one which will print out a ROC curve and a third used to print out a learning curve.


###### 2. Second directory is GetHTMLTags:

This directory contains 8 files. 4 of these files were used to get article counts, titles and urls for analysis purposes. The other 4 files are python scripts used to extract the HTML tags from articles and produce .csv files containing a sorted list of HTML tag frequencies for each article of each source.


###### 3. The third directory is GetContentFeatures:

This directory has 9 python scripts used to extract the attributes for content and title analysis. The features that were extracted from the content and titles of each article include the word count, the article and title sentiment (positive, negative and neutral), bias word count (compared words from a dataset of bias words), stop-word count, exclamation mark count, capitalization count, number count, comma count, quotation count and question mark count. 

###### 4. The fourth directory is WebScraping:

This directory contains the 4 python scripts used obtain the HTML data using the URL links provided in the FakeNewsNet dataset and then prepare that data to be passed into classification algorithms

