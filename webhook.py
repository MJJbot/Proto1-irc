import requests
import json

class api():
    def __init__(self):
        self.header = {'Content-Type' : 'application/json'}
        self.url = 'https://api.twitch.tv/helix/'
    
    def user_id(self, channel, token):
        url = self.url + 'users'
        param = {'login':channel}
        header = {}
        header['Authorization'] = "Bearer "  + token
        response = requests.get(url=url, params=param, headers=header)
        resjson = response.json()
        print(resjson)
        return resjson['data'][0]['id']

    def sub_streamchange(self, id :int, client_id):
        self.header['Client_ID'] = client_id
        data = {}
        data['hub.mode'] = 'subscribe'
        data['hub.topic'] = 'https://api.twitch.tv/helix/streams?user_id=' + str(id)
        data['hub.callback'] = '127.0.0.1:5000/streamChangeCallback'
        data['hub.lease_seconds'] = 86400
        response = requests.post(self.url, data=data, headers=self.header)
        print(response.json)
