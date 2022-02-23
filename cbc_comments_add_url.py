import os
import json

# get new url from command line
new_url = input("Paste url: ")
print("Url is: " + new_url)

# create new story object
new_story = {
    "url": new_url,
    "story_title": "",
    "story_date": "",
    "comment_status": "open",
    "html_to_csv": "no",
    "retrieval_status": "pending",
    "comment_count_site": "",
    "comment_count_retrieved": "0",
    "comment_retrieved_pct": "0",
    "csv_available": ""
}

# open json file
file = os.path.dirname(os.path.abspath(__file__)) + '\cbc_stories.json'
with open(file) as json_file:
    cbc_stories = json.load(json_file)
    #stories = cbc_stories['cbc_stories']
    # append new story to list
    cbc_stories.append(new_story)
    # create new file contents
    new_data = []
    new_data = cbc_stories

# write new file contents
with open(file, 'w') as json_file:
    json.dump(new_data, json_file, indent=4) 

print("Url added to cbc_stories.json")