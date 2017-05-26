# modules
import os
import json
import markdown2
import datetime
import numpy as np
# to fill
json_file = '/home/manuel/trelloTests/trello' # the json file to parse
file_extension = '.html' # the file extension you'd like to use
end_dir = '/home/manuel/trelloTests' # the directory to store your cards
tag = 'artificial movies'
complete_file = tag + file_extension
file_name = os.path.join(end_dir, complete_file)
target = open(file_name, 'w')
# open json
with open(json_file) as data_file:
    data = json.load(data_file)

# variables
cards = data["cards"]
selected_cards = []
cards_dates = []
total_cards = len(data["cards"])
written_cards = 0

# loop
for card in cards:
    if card["desc"].find(tag)!=-1 or card["name"].find(tag)!=-1:
        selected_cards.append(card)
        date  = card["dateLastActivity"][0:card["dateLastActivity"].find('T')]
        cards_dates.append(date)
target.write('<!DOCTYPE html>\n<html>\n<head>\n<style>\ndiv {\nborder: 0px solid black;\nmargin-top: 45px;\nmargin-bottom: 100px;\nmargin-right: 600px;\nmargin-left: 600px;\nbackground-color: white;\n}\n</style>\n</head>\n<body>\n<div>')

dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in cards_dates]
indices = np.argsort(dates)
selected_cards = np.array(selected_cards)[indices]
dates = np.array(dates)[indices]
print(dir(dates[0]))
for card in selected_cards:   
        
    print("Working on: " + card["name"])
    target.write(markdown2.markdown('**'+card["name"]+'**'+'\n'+'-----------------'))
    target.write(markdown2.markdown(card["desc"]))
    target.write(str(dates[written_cards]))
    target.write('##############################################################\n')
    written_cards+=1
    


# message
print("======")
print(str(written_cards) + " out of " + str(total_cards) + " written successfully! :)")
target.write('</div>\n</body>\n</html>')
target.close()

