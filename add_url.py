import os
import json

# get new url from command line
new_url = input("Paste url: ")
print("Url is: " + new_url)

# create new story object
new_story = {
    "url": new_url,
    "retrieval_status": "new",
    "story_status": "open",
    "story_title": "",
    "story_date": "",
    "comment_count_site": "",
    "comment_count_retrieved": "0",
    "comment_retrieved_pct": "0",
    "csv": "no"
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