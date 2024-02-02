"""
consumers are the channels version of django views except for they do more than just respond
the requests from the client. they can also initiate requests to the client all while keeping an open connection
"""
import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """
        initial request that comes in from the client
        """
        return super().connect()
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_establish',
            'message': 'you are connected!'
        }))

    def receive(self, text_data=None, bytes_data=None):
        """
        receive messages from the client
        """
        return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        """
        handle what happen when the client disconnects from this consumers
        """
        return super().disconnect(code)
