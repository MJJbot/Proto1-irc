from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from bot_instance import bot_instance 

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
                bots[channels.index(_channel)].chat.irc.join_channel(_channel)
            else:
                bots.append(bot_instance(_channel))
                channels.append(_channel)
            
            return {'status' : 'success'}
        except Exception as e:
            return {'error' : e}

    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('channel', type=str)
            args = parser.parse_args()
            _channel = args['channel']

            bots[channels.index(_channel)].chat.irc.leave_channel(_channel)
            
            return {'status' : 'success'}
        except Exception as e:
            return {'error' : e}


api.add_resource(CreateBot, '/bot')

if __name__ == '__main__':
    app.run(debug=True)

