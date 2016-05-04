import os

from Options import Options
from filesystem.Filesystem import Filesystem
from protocol.Response import Response
from protocol.HttpRequest import HttpRequest
from BuildBlockManager import BbManager

class HttpGet(HttpRequest):
    def __init__(self, match, csock):
        """
        filepath = match.group(2)
        filename = match.group(3)
	    """
        filename = match.split("/")[-1]
        filepath = match.replace(filename, "")
#        print("File name : " + filename)
#        print("File path : " + filepath)

        if filename is None or filepath is None or filepath is "/":  # directory index requested
            filename = "index.html"
            filepath = "/"
            if Filesystem.file_exists(filepath, filename):  # we look for index.html
                #self.serve_file(filepath, filename, csock)
                with open(Options.root_dir + "/start.html", 'r') as fhandle:
                    start = fhandle.read()
                with open(Options.root_dir + "/end.html", 'r') as fhandle:
                    end = fhandle.read()
                button = BbManager.start("assignments/uge1/")
                msg = start + button + end
                csock.sendall(("""HTTP/1.1 404 Not Found
						 Content-Type: text/html
						 Content-Length: """ + str(len(msg)) + """
						 \n\n""" + msg + """\r\n""").encode())
            else:  # no index file
                Response.reply_404(csock)
        else:  # a file was specified, so we serve it.
            self.serve_file(filepath, filename, csock)
