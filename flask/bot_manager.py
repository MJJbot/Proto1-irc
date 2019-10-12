import twitch
import twitch.helix as helix
from datetime import timedelta
from bot_instance import bot_instance
import threading

helix_api = twitch.Helix('hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True, cache_duration=timedelta(minutes=3))

bots = []
channels = ["kvccdejj", "hanseungho", "pacific8815"]

for i in channels:
    bots.append(bot_instance(i))

def check_onair(channels):
    for i in channels:
        try:
            stream: helix.Stream = helix_api.stream(user_login=i)
        except Exception:
            bots[channels.index(i)].stop_bot()
    # for i in streams.__iter__():
    #     if i.t


threading.Thread(target=check_onair, args=(channels, )).start()


