# modules
import os
import json
import pandas as pd
# # the json file to parse
json_file = '/home/manuel/trello-json-parser/data/Trello_08042020.json'
file_extension = '.txt'  # the file extension you'd like to use
end_dir = '/home/manuel/trello-json-parser/data/'  # dir to store your cards

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

# variables
cards = data["cards"]
card_number = 1
total_cards = len(data["cards"])
written_cards = 0
# list of strings
lst = ['Name', 'Description', 'Assignee', 'Follower', 'Due', 'date',
       'Start date', 'Section/Column', 'Notes']
# Calling DataFrame constructor on list
df_tmp = {'Name': [], 'Description': [], 'Assignee': [], 'Follower': [],
          'Due': [], 'date': [], 'Start date': [], 'Section/Column': [],
          'Notes': []}

# loop
for card in cards:
    print("Working on: " + card["name"])
    complete_file = card["name"] + file_extension
    file_name = os.path.join(end_dir, complete_file)
    target = open(file_name, 'w')
    df_tmp['Name'].append(card["name"])
    df_tmp['Description'].append(card["desc"]+'\n\n'+card['shortUrl'])
    df_tmp['Assignee'].append('mmolano0@hotmail.com')
    df_tmp['Follower'].append('')
    if card["due"] is None:
        due = ''
    else:
        due = card['due'][:10]
    df_tmp['Due'].append(due)
    df_tmp['date'].append(card["dateLastActivity"][:10])
    df_tmp['Start date'].append(card["dateLastActivity"][:10])
    df_tmp['Section/Column'].append(str(card["idList"]))
    df_tmp['Notes'].append('')
    target.write(card["name"]+'\n')
    target.write(card["desc"]+'\n')
    target.close()
    written_cards += 1
    card_number += 1
    if card['name'] == 'visit lab':
        print(card)
    if card['name'] == 'data':
        print(card)

# message
print("======")
df = pd.DataFrame(df_tmp)
df.to_csv(end_dir+'csv_file.csv', index=False)
print(str(written_cards) + " out of " + str(total_cards) +
      " written successfully! :)")
