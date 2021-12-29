import os
import json

# get new url from command line
new_url = input("Paste url: ")
print("Url is: " + new_url)

# create new story object
new_story = {
    "url": new_url,
    "comment_state_data": "new",
    "comment_state_page": "",
    "comment_count_page": "",
    "comment_count_data": "",
    "story_title": "",
    "story_date": ""
}

# open json file
file = os.path.dirname(os.path.abspath(__file__)) + '\cbc_stories.json'
with open(file) as json_file:
    cbc_stories = json.load(json_file)
    stories = cbc_stories['cbc_stories']
    # append new story to list
    stories.append(new_story)
    # create new file contents
    new_data = {}
    new_data['cbc_stories'] = stories

# write new file contents
with open(file, 'w') as json_file:
    json.dump(new_data, json_file, indent=4) 

print("Url added to cbc_stories.json")