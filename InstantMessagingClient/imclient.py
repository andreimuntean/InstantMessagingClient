#!/usr/bin/python2

"""imclient.py: Allows users to connect to a specified server and chat."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

import im
from os import system
from sys import argv
from sys import platform

class IMClient:
    def __init__(self, url):
        self.server = im.IMServerProxy(url)
        self.is_connected = False

    def update(self):
        """Updates the chat."""

        # Fetches the messages.
        messages = filter(lambda key: '_message_' in key, self.server.keys())

        # Clears the screen.
        if platform.startswith('win'):
            system('cls')
        else:
            system('clear')

        # Shows the messages.
        for message in messages:
            # Gets the name of the user.
            name = message[0 : message.find('_')]

            print name + ': ' + self.server[message]

    def send_message(self, message):
        """Sends a message to the server."""

        if self.is_connected:
            # Gets the number of messages on the server.
            message_count = int(self.server['message_count'])

            # Updates the number of messages.
            message_count += 1
            self.server['message_count'] = str(message_count)

            # Sends the message.
            self.server[self.name + '_message_' + str(message_count)] = message
        else:
            print 'User must be logged in to send a message.'

    def connect(self, name):
        """Connects to the server with the specified name."""

        if name.isalnum():
            self.name = name
            self.is_connected = True
        else:
            print 'Name must contain only letters and digits.'

# Gets the server url as an argument.
if len(argv) != 2:
    print 'Error: Server url has not been specified.'
    exit()

# Instantiates the client.
try:
    client = IMClient(argv[1])
except:
    print 'Error: Server url is invalid.'
    exit()

# Connects to the server.
while not client.is_connected:
    client.connect(raw_input('Please enter a name.\n> '))

while True:
    client.update()

    # Gets user input.
    input = raw_input(client.name + '> ')

    if input == '/' or input == '/update' or input == '/refresh':
        continue
    elif input == '/exit':
        break
    else:
        # Sends the message to the server.
        client.send_message(input)