from django.shortcuts import render

# Create your views here.
"""
Channels extend django beyond HTTP to handle websockets, chat protocols, iot protocols
it is build on a python specifications called ASGI (Asynchronouns Server Gateway Interface)

we use channels along with websockets to establish a two-way communication and open connection
between our client and web server

websockets will initiate a connection
channels receive and send request

1- ASGI config
2- consumer
3- Routing
4- WebSockets
"""


def lobby(request):
    return render(request, 'chat/lobby.html')
