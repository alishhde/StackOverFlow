import asyncore
import json
import logging
import socket

from Server.Controller.RequestProcessor import processRequest

clients = []


class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        self.logger = logging.getLogger('SERVER')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(configJson.get('SERVER_QUEUE_SIZE', None))
        self.logger.debug('binding to {}'.format(self.socket.getsockname()))
        self.sockets_list = [self]

    def handle_accept(self):
        sock, address = self.accept()
        clients.append(sock)
        self.logger.debug('new connection accepted')
        EchoHandler(sock)


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        msg = self.recv(configJson.get('RATE', None)).decode("utf-8")
        if msg:
            requests = msg.split('╪')
            self.send(processRequest(requests).encode("utf-8"))
        else:
            self.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s', )

    with open('D:\\My Works\\Projects\\Python Projects\\Project StackOverFlow\\Stackoverflow\\Server\\config.json', 'r') as jsonFile:
        configJson = json.load(jsonFile)
    try:
        logging.debug('Server start')
        server = Server(configJson.get('HOST', None), configJson.get('PORT', None))
        asyncore.loop()
    except Exception as e:
        print(e)
        logging.error('Something happened,\n'
                      'if it was not a keyboard break...\n'
                      'check if address taken, '
                      'or another instance is running. Exit')
    finally:
        logging.debug('Goodbye')
