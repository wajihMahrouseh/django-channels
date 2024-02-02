import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    """
    consumers are the channels version of django views except for they do more than just respond
    the requests from the client. they can also initiate requests to the client all while keeping an open connection.

    each browser has an independent connection with a socket to the server.
    to display messages to all users, we're going to need to enable something called channel layers

    channel layers allow us to create an interaction between different instance of an application for real-time communication

    channel layers are an entirely optional part of django channels and they provide a way for multiple consumers instances to
    talk to each other and other parts of django

    channel layers provides us with groups and channels.
    think of groups like chat rooms that store information about users in a particular room and these rooms will be stored inside of
    an in-memory database inside of these groups we have a bunch of channels also known as users, and channels is a mailbox representing
    a user in a particular group and anybody that knows that specific channels name can send a message to the user via that channel   
    """

    def connect(self):
        """
        initial request that comes in from the client
        """
        self.room_group_name = 'test'  # dynamic value form our url

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_establish',
            'message': 'you are connected!'
        }))

        # return super().connect()

    def receive(self, text_data=None, bytes_data=None):
        """
        receive messages from the client
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

        # return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        """
        handle what happen when the client disconnects from this consumers
        """
        return super().disconnect(code)
