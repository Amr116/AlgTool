from Options import Options


class Response:

    @staticmethod
    def reply_200(csock, content):
        csock.sendall("""HTTP/1.1 200 OK
                         Content-Type: text/html
                         Content-Length: """ + str(len(content)) + """
                         \n\n""" + content + """\r\n""")
        csock.close()

    @staticmethod
    def reply_404(csock):
      """ Not Found error message because file does not exist on server,
          therefore we serve 404.html
      """
      with open(Options.root_dir + "/standardResponse/404.html", 'r') as fhandle:
          content = fhandle.read()
      csock.sendall("""HTTP/1.1 404 Not Found
                       Content-Type: text/html
                       Content-Length: """ + str(len(content)) + """
                       \n\n""" + content + """\r\n""")
      csock.close()
