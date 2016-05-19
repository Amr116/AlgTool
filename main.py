from server.HttpServer import HttpServer

if __name__ == '__main__':
    server = HttpServer('localhost', 8080)
    server.start_server()
