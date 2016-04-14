import socket
import sys
import os

# Carriage Return and Line Feed
CRLF = '\r\n'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
WEBROOT = os.path.join(BASE_DIR, '')

def response_ok(body, mimetype):
    """returns a HTTP response"""
    if body is not None and mimetype is not None:
        resp = []
        resp.append("HTTP/1.1 200 OK")
        resp.append("Content-Type: {}".format(mimetype))
        resp.append("")
        resp.append(body)
    else:
        raise NameError
    return CRLF.join(resp)

def response_not_found():
    """returns a 405 Not Found response"""
    resp = []
    resp.append("HTTP/1.1 404 Not Found")
    resp.append("")
    return CRLF.join(resp)


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("")
    return CRLF.join(resp)

def parse_request(request):
    url = request.split(CRLF, 1)[0]     # url: Uniform Resource Locator
    method, uri, protocol = url.split() # uri: Uniform Resource Identifier

    if method != "GET":
        raise NotImplementedError("We only accept GET!\nSoon we will work on POST")
    return uri
"""
def resolve_uri(uri):
    return 
"""

def server():
    address = 'localhost'
    port    = 8000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #print >>sys.stderr, "making a server on %s:%s" % address
    sock.bind((address,port))
    sock.listen(1)

    try:
        while True:
            conn, addr = sock.accept()
            try:
                request = ""
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        print(len(data))
                        break
                try:
                    uri = parse_request(request)
                except NotImplementedError:
                    response = response_method_not_allowed()
                else:
                    try:
                        content, type = resolve_uri(uri)
                        response = response_ok(content, type)
                    except (NameError, ValueError):
                        response = response_not_found()

                conn.sendall(response)
            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()
        return
if __name__ == '__main__':
    server()
    sys.exit(0)
