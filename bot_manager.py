import twitch
import twitch.helix as helix
from datetime import timedelta
from bot_instance import bot_instance
from flask import Flask, request

app = Flask(__name__)

helix_api = twitch.Helix('hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True, cache_duration=timedelta(minutes=1))

bots = []
channels = ["kvccdejj", "hanseungho"]

for i in channels:
    bots.append(bot_instance(i))

@app.route('/streamChangeCallback')
def streamChangeCallback():
    result = request.data.decode('uft-8')
    if result['data']:
        print("start bot")
        bots[channels.index(result['data'][0]['username'])].start_bot()
    else :
        print("stop bot")
        bots[channels.index(result['data'][0]['username'])].stop_bot()

if __name__ == '__main__':
    app.run(debug=True)