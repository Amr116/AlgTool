import os
import re
import socket
from urllib.parse import urlparse
from protocol.HttpGet import HttpGet
#from protocol.Response import Response

CRLF = '\r\n'
class HttpServer:
    """ This class is responsible to make connection with client side
        by  create ServerSocket object to listen on a specific port
        and handle GET requests.
    """
    host = None
    port = None
    sock = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def start_server(self):
        """ waits until a client starts up and requests a connection on the host and port of this server
            accept client request and call handle_request method
        """
        while True:
            # csock is the client request object
            # caddr is a tuple of the client HOST and PORT
            csock, caddr = self.sock.accept()
            self.handle_request(csock)

    def handle_request(self, csock):
        """ recived Client request with size 8192 bytes
        """
        request = csock.recv(8192).decode()  # returns request headers. (no more than 8kb)
        f = urlparse(request)

        first_line = (request.split(CRLF, 1)[0])

        #print(first_line)
        if len(first_line) > 0:
            fl_split = first_line.split()
            method = fl_split[0]
            uri = fl_split[1]
            protocol = fl_split[2]

            if method == "GET":
                HttpGet(uri, csock)
            """
            For future implementation, We can handle POST Method
            elif method == "POST":
                print("We got to POST Method")
                return
            """
