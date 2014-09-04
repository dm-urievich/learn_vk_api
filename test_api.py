#! /usr/bin/env python3

import vk
import sys
import json

# get access token
#app_id = 4360605
#url = "http://api.vkontakte.ru/oauth/authorize?client_id=" + str(app_id) + "&scope=4&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token"
#webbrowser.open_new_tab(url)
#exit()

vkapi = vk.API(access_token='8bf0a9047f82296483991c51707569cc30dcc605a751f630992470b62f19e1102129c5fcf20ad22130722')

word = sys.argv[1]

result = vkapi.groups.search(q = word, offset = 0, count = 100)

#print(result['count'])
#exit()

json_tree = result['items']

for item in json_tree:
    link = 'http://vk.com/club' + str(item['id'])
    name = item['name']
    full_link = '<a href="' + link + '">' + link + '</a>'
    print(full_link + '\t' + name + '<br>')


