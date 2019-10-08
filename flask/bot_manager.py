from threading import Thread
import time
import irc_bot
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

bots = []
channels = []

class CreateBot(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('channel', type=str)
            args = parser.parse_args()
            _channel = args['channel']

            if _channel in channels:
                bots[channels.index(_channel)].bot.connection.reconnect()
            else:   
                channels.append(_channel)
                run_thread(_channel)

            return {'status' : 'success'}
        except Exception as e:
            return {'error' : e}

    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('channel', type=str)
            args = parser.parse_args()
            _channel = args['channel']
            bots[channels.index(_channel)].bot_stop()
            return {'status' : 'success'}

        except Exception as e:
            return {'error' : e}



api.add_resource(CreateBot, '/bot')

def run_thread(channel):
    bot = irc_bot.botThread(channel)
    bots.append(bot)
    bot.start()
    return 


if __name__ == '__main__':
    app.run(debug=True)
# def disconn_bot(channel, thread):
#     thread.


    
# for proc in processes:
#     proc.communicate()

