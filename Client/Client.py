import asyncore
import collections
import json
import logging
import socket
import sys
import threading
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

with open('D:\My Works\Projects\Python Projects\Project StackOverFlow\Stackoverflow\Client\config.json', 'r') as jsonFile:
    configJson = json.load(jsonFile)

response = None


class Client(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.log = logging.getLogger('Client')
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log.info('Connecting to host at %s', (host, port))
        self.connect((host, port))
        self.outbox = collections.deque()

    def sendRequest(self, message):
        self.outbox.append(message)
        self.log.info('Enqueued message: %s', message)

    def handle_write(self):
        if not self.outbox:
            return
        message = self.outbox.popleft()
        if len(message) > configJson.get('RATE', None):
            raise ValueError('Message too long')
        self.send(message)

    def handle_read(self):
        global response
        message = self.recv(configJson.get('RATE', None)).decode("utf-8")
        self.log.info('Received message: %s', message)
        response = message


# class Client(asyncore.dispatcher_with_send):
#
#     def __init__(self, host, port, message, pk):
#         self.logger = logging.getLogger('CLIENT')
#         asyncore.dispatcher.__init__(self)
#         self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.host = host
#         self.port = port
#         self.connect((host, port))
#         self.out_buffer = message
#         self.clientID = pk
#         self.rec_msg = ""
#         self.logger.debug('Connected #{}'.format(self.clientID))
#
#     def handle_close(self):
#         self.close()
#
#     def handle_read(self):
#         self.rec_msg = self.recv(configJson.get('RATE', None)).decode("utf-8")
#         print(self.rec_msg)
#         self.close()

client = Client(configJson.get('HOST', None), configJson.get('PORT', None))


def requestFactory(request):
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s', )

    try:
        client.sendRequest(request.encode("utf-8"))
        thread = threading.Thread(target=asyncore.loop)
        thread.start()
        time.sleep(0.5)
        return response
    except Exception as Ex:
        print(Ex)


if __name__ == "__main__":
    from View.WelcomePage import WelcomeScreen

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    welcome = WelcomeScreen(widget)
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
