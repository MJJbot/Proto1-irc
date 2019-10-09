import twitch

def handle_message(message: twitch.chat.Message) -> None:
    if message.text.startswith("!하이"):
        message.chat.send("하이요")

class bot_instance:
    def __init__(self, channel):
        self.chat = twitch.Chat(channel=channel,
                       nickname='bot',
                       oauth='oauth:///',
                       helix=twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True))
        self.chat.subscribe(handle_message)

