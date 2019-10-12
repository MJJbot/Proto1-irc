import twitch
import logging
from typing import Optional
import twitch.helix as helix

class bot_instance:
    def __init__(self, channel):
        self.channel = channel
        self.chat = twitch.Chat(channel=channel,
                       nickname='bot',
                       oauth='oauth:la6kj4pn3vzfdvvkfrg8y5eqvbuxjk',
                       helix=twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True))
        self.chat.subscribe(self.handle_message)
        print("Enter" + self.channel)
        self.buf = []

    def handle_message(self, message: twitch.chat.Message) -> None:
        self.buf.append(message.sender + ":" + message.text + "\n")
    
    def stop_bot(self):
        helix = twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True)
        try:
            timestamp = helix.stream(user_login=self.channel).started_at
        except:
            return
        file = open(self.channel+"_"+timestamp+".txt", w, encoding='utf-8')
        file.write(''.join(self.buf))
        self.chat.irc.leave_channel(self.channel)

