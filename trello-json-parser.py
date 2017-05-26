# modules
import os
import json

# to fill
json_file = 'C:\\Users\\molano\\Desktop\\trello.txt' # the json file to parse
file_extension = '.txt' # the file extension you'd like to use
end_dir = 'C:\\Users\\molano\\Desktop\\trelloTest' # the directory to store your cards

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

# variables
cards = data["cards"]
print(data.keys())
card_number = 1
total_cards = len(data["cards"])
written_cards = 0

# loop
for card in cards:
    print("Working on: " + card["name"])
    complete_file = 'card' + str(card_number) + file_extension
    file_name = os.path.join(end_dir, complete_file)
    target = open(file_name, 'w')
    target.write(card["name"]+'\n')
    target.write(card["desc"]+'\n')
    target.close()
    written_cards+=1
    card_number+=1

# message
print("======")
print(str(written_cards) + " out of " + str(total_cards) + " written successfully! :)")
