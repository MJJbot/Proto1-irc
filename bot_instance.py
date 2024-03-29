import twitch

def handle_message(message: twitch.chat.Message) -> None:
    if message.text.startswith("!"):
        return

class bot_instance:
    def __init__(self, channel):
        self.chat = twitch.Chat(channel=channel,
                       nickname='bot',
                       oauth='oauth:la6kj4pn3vzfdvvkfrg8y5eqvbuxjk',
                       helix=twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True))
        self.chat.subscribe(handle_message)
    
