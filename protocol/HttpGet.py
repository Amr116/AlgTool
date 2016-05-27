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
                (BuildBlockButton, BuildBlockScreen) = BbManager.start("assignments/week2/")

                with open(Options.root_dir + "/template/header.html", 'r') as fhandle:
                    Header = '<!DOCTYPE html>\n<html lang="en">\n' + fhandle.read()

                with open(Options.root_dir + "/template/topbar.html", 'r') as fhandle:
                    topbar = '<body>\n<div class="container-fluid">\n' + fhandle.read()

                ButtonMenu = '<div class="row down-container">\n<div class="col-lg-3">\n<div class="row cluster">' + \
                            BuildBlockButton + '</div>\n</div>\n'

                with open(Options.root_dir + "/template/algoscreen.html", 'r') as fhandle:
                    AlgorithmScreen = fhandle.read()

                with open(Options.root_dir + "/template/logcontainer.html", 'r') as fhandle:
                    LogContainer = fhandle.read() + '</div>\n'

                ShowBBInScreen = 'function insert(id){\n switch (id) {\n' + \
                                 BuildBlockScreen + '}\n return str;\n}'

                with open(Options.root_dir + "/template/functions.js", 'r') as fhandle:
                    Functions = '<script type = "text/javascript">\n' + \
                                fhandle.read() + ShowBBInScreen + \
                                '</script>'

                with open(Options.root_dir + "/template/tail.html", 'r') as fhandle:
                    Tail = fhandle.read() + '</body>\n</html>'

                CompletePage = Header + topbar + ButtonMenu + AlgorithmScreen + LogContainer + Functions + Tail
                csock.sendall(("""HTTP/1.1 200 OK
						 Content-Type: text/html
						 Content-Length: """ + str(len(CompletePage)) + """
						 \n\n""" + CompletePage + """\r\n""").encode())
            else:  # no index file
                Response.reply_404(csock)
        else:  # a file was specified, so we serve it.
            self.serve_file(filepath, filename, csock)
