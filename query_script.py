# Script to query against json objects
# Marc Schmitt
import csv
import json

# parser = argparse.ArgumentParser(description='Takes a json file + keywords and searches against it.')

# parser.add_argument('json file', type='String')

# article_file_path = input('Please input path to json file of articles\n')
string_query = input('Please input keyword to search for\n')
article_file_path = 'filtered_articles.json'
# string_query = 'human rights'

count = 0

with open(article_file_path) as articlesFile:
    data = json.load(articlesFile)
    results = []
    for art in data:
        # print(art)
        if (string_query in art['text']):
            count += 1
            results.append(art)

fileName = string_query + '.json'
with open(fileName, 'w+') as resultsFile:

    # json.dump(, resultsFile, indent=4)
    json.dump([{'Search Term':string_query,'Count':count}] + results, resultsFile, indent=4)

csvFileName = string_query + '.csv'
with open(csvFileName, 'w') as csvFile:
    f = csv.writer(csvFile)

    # Write CSV Header, If you dont need that, remove this line
    # f.writerow(["Title", "Official Name", "Official Title", "Date", "Text"])
    f.writerow(["Title", "Official Name", "Date", "Text"])

    for x in results:
        # f.writerow([x['title'], x['official_name'], x['official_title'], x['date'], x['text']])
        f.writerow([x['title'], x['official_name'], x['date'], x['text']])