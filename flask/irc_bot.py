# # -*- coding: utf-8 -*- 
# import irc.bot  
# import requests  
# import abc
# from threading import Lock, Thread, Event
  
  
# class TwitchBot(irc.bot.SingleServerIRCBot):  
#     def __init__(self, username, client_id, token, channel):  
#         self.client_id = client_id  
#         self.token = token  
#         self.channel = "#" + channel
#         self.running = True
#         #IRC bot 
        
#         server = 'irc.chat.twitch.tv'  
#         port = 6667 
#         irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], username, username)

  
#     def on_welcome(self, c, e):  
#         print(self.channel + '에 연결되었습니다.')
#         c = self.connection
#         c.privmsg(self.channel, "하이염")
#         #c.cap('REQ', ':twitch.tv/membership')
#         #c.cap('REQ', ':twitch.tv/tags')
#         c.cap('REQ', ':twitch.tv/commands')
#         c.join(self.channel)

#     def on_pubmsg(self, c, e): 
#         print('From ' + self.channel + ', Received msg: '+ e.arguments[0])
#         if e.arguments[0][:1] == '!':
#             cmd = e.arguments[0].split(' ')[0][1:]
#             print('Received command: ' + cmd)
#             #self.do_command(e, cmd)
#         return

#     def bot_disconnect(self, c, e):
#         print(self.channel + '에서 퇴장합니다.')
#         self.reactor.connection_class.disconnect("QUIT")


#     # def do_command(self, e, cmd):  
#     #     c = self.connection  
#     # #     # Poll the API to get current game.  
#     #     if cmd == "game":  
#     #         url = 'https://api.twitch.tv/kraken/channels/' + self.channel
#     #         headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}  
#     #         r = requests.get(url, headers=headers).json()  
#     #         c.privmsg(self.channel, r['display_name'] + ' is currently playing ' + r['game'])  
  
#     #     # Poll the API the get the current status of the stream  
#     #     elif cmd == "title":  
#     #         url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id  
#     #         headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}  
#     #         r = requests.get(url, headers=headers).json()  
#     #         c.privmsg(self.channel, r['display_name'] + ' channel title is currently ' + r['status'])  
  
#     #     # The command was not recognized  
#     #     else:  
#             # c.privmsg(self.channel, "Did not understand command: " \+ cmd)
    

# class StoppableThread(Thread):
#     """Thread class with a stop() method. The thread itself has to check
#     regularly for the stopped() condition."""

#     def __init__(self):
#         super(StoppableThread, self).__init__()
#         self._stop_event = Event()

#     def stop(self):
#         self._stop_event.set()

#     def stopped(self):
#         return self._stop_event.is_set()
    


# class botThread(StoppableThread):
#     def __init__(self, channel):
#         StoppableThread.__init__(self)
#         self.username = "kvccdejj"
#         self.client_id = "hqiwd4o8a3mf6l7t7l0xge8qt7ksob" 
#         self.token = "la6kj4pn3vzfdvvkfrg8y5eqvbuxjk" 
#         self.channel = channel 
#         self.bot = TwitchBot(self.username, self.client_id, self.token, self.channel)
#         #self.thread = Thread(target=self.bot.start, daemon=True)
#         self.status = 1

#     #def bot_start(self):  
#         #self.bot = TwitchBot(username, client_id, token, channels)
#         #self.bot.start()
#         #self.thread.start()

#         # def bot_start(self):
#         #     self.a.start()
#     def bot_stop(self):
#         self.bot.connection.quit("QUIT")
#         self.stop()

#     def run(self):
#         self.bot.start()



# class reconnectStrategy(irc.bot.ReconnectStrategy):
#     def run(self, bot):
#         return

