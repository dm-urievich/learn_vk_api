#! /usr/bin/env python3

import vk
import sys
import json

# get access token
#app_id = 4360605
#url = "http://api.vkontakte.ru/oauth/authorize?client_id=" + str(app_id) + "&scope=4&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token"
#webbrowser.open_new_tab(url)
#exit()

word = sys.argv[1]

txt_file = open(word + '.txt', "w")
html_file = open(word + '.html', "w")

vkapi = vk.API(access_token='copy_token_here')

result = vkapi.groups.search(q = word, offset = 0, count = 100)

#print(result['count'])
#exit()

json_tree = result['items']

for item in json_tree:
    link = 'http://vk.com/club' + str(item['id'])
    name = item['name']
    tag_link = '<a href="' + link + '">' + link + '</a>' + '\t' + name + '<br>'
    txt_file.write(link + '\n')
    html_file.write(tag_link + '\n')

txt_file.close()
html_file.close()
