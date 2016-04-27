from server.HttpServer import HttpServer

if __name__ == '__main__':
    server = HttpServer('localhost', 8000)
    server.start_server()
