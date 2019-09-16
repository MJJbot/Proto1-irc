# -*- coding: utf-8 -*- 
import sys  
import irc.bot  
import requests  
from threading import Lock, Thread
  
  
class TwitchBot(irc.bot.SingleServerIRCBot):  
    mutex = Lock()

    def __init__(self, username, client_id, token, channel):  
        self.client_id = client_id  
        self.token = token  
        self.channel = "#" + channel
        self.hogumastack = 0 
        self.running = True
        #TwitchBot.mutex.acquire()
        #IRC bot 
        server = 'irc.chat.twitch.tv'  
        port = 6667 
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], username, username)

        #witchBot.mutex.release()

  
    def on_welcome(self, c, e):  
        print(self.channel + '에 연결되었습니다.')  

        #c.cap('REQ', ':twitch.tv/membership')  
        #c.cap('REQ', ':twitch.tv/tags')  
        c.cap('REQ', ':twitch.tv/commands')  
        c.join(self.channel)  
  
    def on_pubmsg(self, c, e): 
        #print('Received msg: '+ e.arguments[0])  
        if e.arguments[0][:1] == '!':  
            cmd = e.arguments[0].split(' ')[0][1:]  
            print('Received command: ' + cmd)  
            #self.do_command(e, cmd)  
        return  

  
    # def do_command(self, e, cmd):  
    #     c = self.connection  
    #     # Poll the API to get current game.  
    #     if cmd == "game":  
    #         url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id  
    #         headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}  
    #         r = requests.get(url, headers=headers).json()  
    #         c.privmsg(self.channel, r['display_name'] + ' is currently playing ' + r['game'])  
  
    #     # Poll the API the get the current status of the stream  
    #     elif cmd == "title":  
    #         url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id  
    #         headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}  
    #         r = requests.get(url, headers=headers).json()  
    #         c.privmsg(self.channel, r['display_name'] + ' channel title is currently ' + r['status'])  
  
    #     # Provide basic information to viewers for specific commands        
    #     elif cmd == "스팀잇":
    #         message = "안녕! 스팀잇!"
    #         c.privmsg(self.channel, message)  
  
    #     # The command was not recognized  
    #     else:  
            # c.privmsg(self.channel, "Did not understand command: " \+ cmd)
    

def main(channel):  
    username = "kvccdejj" 
    client_id = "hqiwd4o8a3mf6l7t7l0xge8qt7ksob" # Client ID  
    token = "la6kj4pn3vzfdvvkfrg8y5eqvbuxjk" # oauth: 는 빼고 뒷부분만 적어주시면 됩니다.  
    channels = channel#str(sys.argv[1])
    a = TwitchBot(username, client_id, token, channels)
    a.start()
    # while running:
    #     command = input("")
    #     if command == "exit":
    #         running = False
    #         for i in range(0, len(channel)):
    #             bots[i].running = False`
    
if __name__ == "__main__":  
    main()
