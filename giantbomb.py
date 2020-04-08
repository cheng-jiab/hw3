import urllib
import requests
import json
import csv
import pymongo

import pymongo
client = pymongo.MongoClient('mongodb+srv://m220student:m220password@mflix-6auna.mongodb.net/test?retryWrites=true&w=majority')

hw03 = client.hw03
game = hw03.game

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent,}
'''
###url = 'https://www.giantbomb.com/api/accessory/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json&limit=1'
url = 'http://www.giantbomb.com/api/companies/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json&limit=100&offset=900'
#######url = 'https://www.giantbomb.com/api/games/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json&limit=100&sort=date_last_updated:desc&filter=platforms:PlayStation4'
###url = 'http://www.giantbomb.com/api/company/3010-1/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json'
#game #url = 'https://www.giantbomb.com/api/game/3030-66000/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json'
print(url)
req = urllib.request.Request(url=url, headers=headers)
json_obj = urllib.request.urlopen(req)
data = json.load(json_obj)
#print(json_obj.read())
#result = (data)['Results']
#print(data['results'])

print(data['results'])
for i in data['results']:
    save = (i['name'],i['guid'],i['aliases'],i['deck'],i['date_last_updated'],i['date_founded'])
    with open('gamelist.csv', 'a')as r:
        r_csv = csv.writer(r)
        r_csv.writerow(save)
'''
with open('companylist.csv')as comp:
    c_csv = csv.reader(comp)
    mongodb = []
    for c in c_csv:
        url ='http://www.giantbomb.com/api/company/'+ c[1] + '/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json'
        #print(url)
        req_c = urllib.request.Request(url=url, headers=headers)
        json_obj_c = urllib.request.urlopen(req_c)
        data_c = json.load(json_obj_c)
        res = data_c['results']
        for i in res['published_games'][1:10]:
            url_g = i['api_detail_url'] + '?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json'
            print(i['name'])
            req_g = urllib.request.Request(url=url_g, headers=headers)
            json_obj_g = urllib.request.urlopen(req_g)
            data_g = json.load(json_obj_g)
            res_g = data_g['results']g
            print(res_g)


            mongodb.append(res_g)
            #print(mongodb)


game.insert_many(mongodb)
'''
for i in data['results']:
#    row = i['guid']
    url_c = 'http://www.giantbomb.com/api/company/'+ str(i['guid'])+'/?api_key=75a93f4b071b6002e1f328293149fb3cd166b91a&format=json'
    req_c = urllib.request.Request(url=url_c, headers=headers)
    json_obj_c = urllib.request.urlopen(req_c)
    data_c = json.load(json_obj_c)
    res = data_c['results']
    try:
        for game in res['published_games'][1:5]:
            save = game['api_detail_url'],game['name'],res['guid'],res['name']
            print(save)
            with open('game.csv', 'a')as r:
                r_csv = csv.writer(r)
                r_csv.writerow(save)
'''
