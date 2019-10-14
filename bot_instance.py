import twitch
import logging
import twitch.helix as helix
import twitch.chat as chat
import webhook

class bot_instance:
    def __init__(self, channel):
        self.channel = channel
        api = webhook.api()
        self.id = api.user_id(channel, 'la6kj4pn3vzfdvvkfrg8y5eqvbuxjk') #la6kj4pn3vzfdvvkfrg8y5eqvbuxjk   qxhcdwsgg5m3qm7or17f3lo51soznk
        api.sub_streamchange(id, 'hqiwd4o8a3mf6l7t7l0xge8qt7ksob')
        
        self.helix=twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True)
        self.chat = twitch.Chat(channel=channel,
                       nickname='bot',
                       oauth='oauth:la6kj4pn3vzfdvvkfrg8y5eqvbuxjk',
                       helix=self.helix)
        self.buf = []
            
    def handle_message(self, message: twitch.chat.Message) -> None:
        self.buf.append(message.sender + ":" + message.text + "\n")
        print(message.sender + ":" + message.text + "\n")

    def stop_bot(self):
        file = open(self.channel+".txt", "w", encoding='utf-8')
        file.write(''.join(self.buf))
        self.buf.clear()
        self.chat.dispose()

    def start_bot(self):
        self.chat.subscribe(self.handle_message)

