# modules
import os
import json
import pandas as pd
# # the json file to parse
# names = ['Trello_08042020.json', 'NAFC_task_08042020.json', 'CV_08042020.json']
names = ['Trello_08042020.json']
sv_names = ['Expectations_08042020']
file_extension = '.txt'  # the file extension you'd like to use
end_dir = '/home/manuel/trello-json-parser/data/'  # dir to store your cards
year_limit = 2018

for ind_name, name in enumerate(names):
    print(name)
    json_file = '/home/manuel/trello-json-parser/data/'+name

    # open json
    with open(json_file) as data_file:
        data = json.load(data_file)

    # variables
    cards = data["cards"]
    total_cards = len(data["cards"])
    written_cards = 0
    # list of strings
    # Calling DataFrame constructor on list
    df_tmp = {'Name': [], 'Description': [], 'Assignee': [],
              'Follower': [], 'Due': [], 'date': [], 'Start date': [],
              'Section/Column': [], 'Notes': [], 'Completed At': [], 'Tags': []}
    # relevant_projects = ['paper/book', 'RNN project', 'students', 'DMS',
    #  'Expectations', 'metaWork', 'NeuroGym']
    # loop
    disc_sects = ['565febb3fabcb515abac1dfd']
    sel_lbl = ['Expectations']
    for card in cards:
        year = float(card["dateLastActivity"][:4])
        # process labels
        labels = ''
        lbl_in = False
        for item in card['labels']:
            labels += item['name'] + ','
            if item['name'] in sel_lbl:
                lbl_in = True
        process_card =\
            year >= year_limit and card['idList'] not in disc_sects and lbl_in
        if process_card:
            # NAME
            df_tmp['Name'].append(card["name"])
            # DESCRIPTION
            df_tmp['Description'].append(card["desc"])
            # ASSIGNEE
            df_tmp['Assignee'].append('')
            # FOLLOWERS
            df_tmp['Follower'].append('')
            # DUE DATE
            if card["due"] is None:
                due = ''
            else:
                due = card['due'][:10]
            df_tmp['Due'].append(due)
            df_tmp['date'].append(card["dateLastActivity"][:10])
            df_tmp['Start date'].append(card["dateLastActivity"][:10])
            # NOTES (add trello url)
            df_tmp['Notes'].append(card['shortUrl'])
            # WHEN WAS COMPLETED (not processed by asana)
            if card['closed']:
                # df_tmp['Completed At'].append(card["dateLastActivity"][:10])
                df_tmp['Completed At'].append('')
            else:
                df_tmp['Completed At'].append('')
            written_cards += 1
            # TAGS (not processed by asana)
            df_tmp['Tags'].append(labels[:-1])
            # ASSIGN TO SPECIFIC COLUMN
            if card['closed']:
                df_tmp['Section/Column'].append('Done')
            elif card['idList'] == '5703e6e28a257311cab6c1f2':
                df_tmp['Section/Column'].append('Papers/books')
            elif card['idList'] == '5d9db08e1c943d86fc9174f7':
                df_tmp['Section/Column'].append('Useful stuff')
            elif card['idList'] == '565374092595fae22d8a1832':
                df_tmp['Section/Column'].append('To-do')
            elif card['idList'] == '5653740e7b1cf15997807b3f':
                df_tmp['Section/Column'].append('Doing')
            elif card['idList'] == '5653741a546f5787b821970b':
                df_tmp['Section/Column'].append('Ideas')
            else:
                df_tmp['Section/Column'].append(str(card["idList"]))
            if card['name'] == 'NY':
                print(card.keys())
                print(card["idList"])
    # message
    df = pd.DataFrame(df_tmp)
    df.to_csv(end_dir+'csv_file_'+sv_names[ind_name]+'.csv', index=False)
    print(str(written_cards) + " out of " + str(total_cards) +
          " written successfully! :)")
    print("======")
