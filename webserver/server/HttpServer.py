import socket
import re
from protocol.HttpGet import HttpGet

CRLF = '\r\n'
class HttpServer:

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
        while True:
	    # csock : is the client request object
            # caddr : is a tuple of the client HOST and PORT
            csock, caddr = self.sock.accept()
            self.handle_request(csock)

    def handle_request(self, csock):
        request = csock.recv(8192)  # returns request headers. (no more than 8kb)

#        match = re.match("(\w+)\s(?:/|(.*)(/[\w\d]+\.html?))\sHTTP/1", request)
        first_line = request.split(CRLF, 1)[0]
	method, uri, protocol = first_line.split()

        if method == "GET":
            HttpGet(uri, csock)
        elif method == "POST":
            print("We did not implement POST")
            return

