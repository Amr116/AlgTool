import os

from Options import Options
from response.Response import Response
from protocol.HttpRequest import HttpRequest
from BuildBlockManager import BbManager

class HttpGet(HttpRequest):

    def __init__(self, match, csock):

        filename = match.split("/")[-1]
        if filename.endswith(".html") or filename.endswith(".js") or filename.endswith(".css") or filename.endswith(".png"):
            filename = filename
        else:
            filename = ""

        filepath = match.replace(filename, "")



        if (((filename == "index.html") or (filename == "")) and (filepath == "") or (filepath == "/")):
             filename = "index.html"
             filepath = "/"
             self.serve_index(csock)
        elif (filename.endswith(".css")):
            self.serve_file(filepath, filename, csock)

        elif ( filename.endswith(".js")):
            self.serve_file(filepath, filename, csock)
        elif ( filename.endswith(".png")):
            self.serve_file(filepath, filename, csock)


        elif (filename is "" or filename == "index.html") and (os.path.isdir(filepath[1:])):
            (BuildBlockButton, BuildBlockScreen, Evaluation_Function) = BbManager.start(filepath[1:])

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

            with open(Options.root_dir + "/template/functions.js", 'r') as fhandle:
                Functions = '<script type = "text/javascript">\n' + \
                            fhandle.read() + BuildBlockScreen + Evaluation_Function + \
                            '</script>'

            with open(Options.root_dir + "/template/tail.html", 'r') as fhandle:
                Tail = fhandle.read() + '</body>\n</html>'

            CompletePage = Header + topbar + ButtonMenu + AlgorithmScreen + LogContainer + Functions + Tail
            self.serve_media(CompletePage, csock)
        else:
             self.serve_index(csock)

