import json
import csv

with open('./lexProject/all_links.json') as f:
    data = json.load(f)

with open('filtered_links.json', 'w') as outfile:    
    count = 0
    forCsv = []
    for dat in data:
        if(dat['date']):
            count += 1
            print(count)
            forCsv.append(dat)
            
    json.dump(forCsv, outfile,indent=4)

# with open('filtered_links.csv', 'w') as csvFile:
#     f = csv.writer(csvFile)

#     # Write CSV Header, If you dont need that, remove this line
#     # f.writerow(["Title", "Official Name", "Official Title", "Date", "Text"])
#     f.writerow(["Title", "Official Name", "Date"])

#     for x in forCsv:
#         # f.writerow([x['title'], x['official_name'], x['official_title'], x['date'], x['text']])
#         f.writerow([x['title'], x['official_name'], x['date']])