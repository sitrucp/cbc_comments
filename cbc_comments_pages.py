from cbc_paths import file_path_page, file_path_image
import os
import json

# get all complete urls
cbc_stories_file = os.path.dirname(os.path.abspath(__file__)) + '\cbc_stories.json'
with open(cbc_stories_file) as json_file:
    cbc_stories = json.load(json_file)

all_complete_stories = ([x for x in cbc_stories if x['viz_available'] == 'yes' and x['audit_status'] == 'complete'])

print(len(all_complete_stories), "complete stories")
print(all_complete_stories[-1]['url'])

# loop to get all url comment counts and see if comments closed
# write results to the url file

# CREATE INDEX PAGE
f_index = open(os.path.dirname(os.path.abspath(__file__)) + '\index.html','w')
# create index content
url_list = ''
for story in all_complete_stories:
    cbc_url = story['url']
    file_name = cbc_url.replace('https://www.cbc.ca/','').replace('news/','').replace('sports/','').replace('/','_')
    url_list = url_list + '<p>' + story['story_date'] + ' - <a href="https://sitrucp.github.io/cbc_comments/page/' + file_name + '.html">'+ story['story_title'] +'</a></p>' 
f_index_content = '<html>' \
'<head>' \
'<title>CBC Comments Analysis</title>' \
'<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />' \
'<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
'</head>' \
'<body style="margin: 20px;">' \
'<p><a href="https://github.com/sitrucp/cbc_comments">Github repository</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/image_grid.html">Image grid</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/page/all_stories.html">All stories analysis</a></p>' \
'<h1>CBC Story Comments Analysis</h1>' \
'<p>Click link to view visualizations</p>' \
 + url_list + \
'</body>' \
'</html>'
# save and close index page
f_index.write(f_index_content)
f_index.close()

# CREATE STORY PAGES
for story in all_complete_stories:
    # create file name stem
    cbc_url = story['url']
    file_name = cbc_url.replace('https://www.cbc.ca/','').replace('news/','').replace('sports/','').replace('/','_')
    # create new page
    f_page = open(file_path_page + file_name + '.html','w')
    # create page content
    f_page_content = '<html>' \
    '<head>' \
    '<title>CBC Comments Analysis: ' + story['story_title'] + '</title>' \
    '<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />' \
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
    '</head>' \
    '<body style="margin: 20px;">' \
    '<p><a href="https://github.com/sitrucp/cbc_comments">Github repository</a></p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/">Story list</a></p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/image_grid.html">Image grid</a></p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/page/all_stories.html">All stories analysis</a></p>' \
    '<h1>CBC Story Comments Analysis</h1>' \
    '<H2>' + story['story_date'] + ' - ' + story['story_title'] + '</H2>' \
    '<p><a href="' + cbc_url + '" target="_blank">CBC story link</a></p>' \
    '<H2>Word cloud top 200 comment words</H2>' \
    '<p>Word size is relative to # of occurences in comments.</p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/image/word_cloud_' + file_name + '.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/word_cloud_' + file_name + '.png" width="600"/></a></p>' \
    '<H2>Word cloud top 100 comment usernames</H2>' \
    '<p>Username size is relative to # of comments.</p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/image/people_' + file_name + '.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/people_' + file_name + '.png" width="600"/></a></p>' \
    '<H2>Comment and reply username interactions</H2>' \
    '<p>Red circle = username (size relative to # comments).<br>' \
    'Blue lines = interactions between usernames (width relative to # interactions).</p>' \
    '<p><a href="https://sitrucp.github.io/cbc_comments/image/network_' + file_name + '.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/network_' + file_name + '.png" width="600"/></a></p>' \
    '</body>' \
    '</html>'
    f_page.write(f_page_content)
    f_page.close()

# CREATE GRID PAGE 
f_grid = open(os.path.dirname(os.path.abspath(__file__)) + '\image_grid.html','w')
# create image_grid content
grid_div_list = ''
for story in all_complete_stories:
    cbc_url = story['url']
    file_name = cbc_url.replace('https://www.cbc.ca/','').replace('news/','').replace('sports/','').replace('/','_')
    # create div with image inside, link to image page
    grid_div_list = grid_div_list + '<div class="image_div" style="float: left; padding: 5px; width: 210px; height: 265px;">' \
        '<a href="https://sitrucp.github.io/cbc_comments/image/network_' + file_name + '.png" target="_blank">' \
        '<img src="https://sitrucp.github.io/cbc_comments/image/network_' + file_name + '.png" width="200" alt="'+ story['story_title'] +'"/></a>' \
        '<br><a style="font-size: 10px;" href="https://sitrucp.github.io/cbc_comments/page/' + file_name + '.html">Analysis</a> - ' \
        '<a style="font-size: 10px;" href="' + cbc_url + '" target="_blank">CBC link</a> - ' \
        '<a style="font-size: 10px;" href="https://sitrucp.github.io/cbc_comments/image/network_' + file_name + '.png" target="_blank">Zoom</a>' \
        '<br><p style="font-size: 10px;">' + story['story_date'] + ' - ' + story['story_title'] + '</p>' \
        '</div>'
f_grid_content = '<html>' \
'<head>' \
'<title>CBC Comments Username Interaction Visualizations</title>' \
'<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />' \
'<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
'</head>' \
'<body style="margin: 20px;">' \
'<p><a href="https://github.com/sitrucp/cbc_comments">Github repository</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/">Story list</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/page/all_stories.html">All stories analysis</a></p>' \
'<h1>CBC Comments Username Interaction Visualizations</h1>' \
'<p>Red circle = username (size relative to # comments).<br>' \
'Blue lines = interactions between usernames (width relative to # interactions).</p>' \
'<div class="grid_container">' + grid_div_list + '</div>'\
'</body>' \
'</html>'
# save and close index page
f_grid.write(f_grid_content)
f_grid.close()

# CREATE ALL STORIES PAGE
from cbc_paths import file_path_csv, file_path_image
import glob
all_files = glob.glob(os.path.join(file_path_csv, "*.csv"))
story_count = str(len(all_files))

# create new page
f_page = open(file_path_page + 'all_stories' + '.html','w')
# create page content
f_page_content = '<html>' \
'<head>' \
'<title>CBC Comments Analysis: All Stories</title>' \
'<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />' \
'<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
'</head>' \
'<body style="margin: 20px;">' \
'<p><a href="https://github.com/sitrucp/cbc_comments">Github repository</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/">Story list</a></p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/image_grid.html">Image grid</a></p>' \
'<h1>CBC Story Comments Analysis</h1>' \
'<p>This page shows combined analysis of ' + story_count + ' stories.</p>' \
'<H2>Word cloud top 200 comment words</H2>' \
'<p>Word size is relative to # of occurences in comments.</p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/image/word_cloud_all.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/word_cloud_all.png" width="600"/></a></p>' \
'<H2>Word cloud top 100 comment usernames</H2>' \
'<p>Username size is relative to # of comments.</p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/image/people_all.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/people_all.png" width="600"/></a></p>' \
'<H2>Comment and reply username interactions</H2>' \
'<p>This shows username interactions across all of the ' + story_count + ' stories for all usernames that commented in one or more stories.</p>' \
'<p>Red circle = usernames (size relative to # comments).<br>' \
'Blue lines = comments and replies between usernames (width relative to # comments and replies).</p>' \
'<p><a href="https://sitrucp.github.io/cbc_comments/image/network_all.png" target="_blank"><img src="https://sitrucp.github.io/cbc_comments/image/network_all.png" width="600"/></a></p>' \
'</body>' \
'</html>'
f_page.write(f_page_content)
f_page.close()