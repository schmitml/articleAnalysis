# Script to query against json objects
# Marc Schmitt
from tkinter import *
import argparse
import json


# parser = argparse.ArgumentParser(description='Takes a json file + keywords and searches against it.')

# parser.add_argument('json file', type='String')

# article_file_path = input('Please input path to json file of articles\n')
# string_query = input('Please input keyword to search for\n')
article_file_path = 'filtered_links.json'
string_query = 'human rights'

count = 0

with open(article_file_path) as articlesFile:
    data = json.load(articlesFile)
    results = []
    for art in data:
        # print(art)
        if (string_query in art['text']):
            count += 1
            results.append(art)

with open('search_results.json', 'w+') as resultsFile:

    # json.dump(, resultsFile, indent=4)
    json.dump([{'Search Term':string_query,'Count':count}] + results, resultsFile, indent=4)

