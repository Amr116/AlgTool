from Options import Options
from filesystem.Filesystem import Filesystem
from response.Response import Response
import os


class HttpRequest:

    def serve_file(self, filepath, filename, csock):
        exists = Filesystem.file_exists(filepath, filename)
        if exists:
            with open(Options.root_dir + filepath + filename, 'r') as fhandle:
                Response.reply_200(csock, fhandle.read())
        else:
            Response.reply_404(csock)

    def serve_media(self, filepath, filename, csock):
        exists = Filesystem.file_exists(filepath, filename)
        if exists:
            with open(Options.root_dir + filepath + filename, 'r') as fhandle:
                Response.reply_200(csock, fhandle.read())
        else:
            Response.reply_404(csock)

    def serve_index(self):
        fd = "assignments"
        data = os.listdir(fd)
        data_list = []
        serve_data= ""
        for i in data:
            data_list.append(os.path.join(fd, i))

        for j in data_list:
            serve_data += "<a class='opgaver' href='/"+str(j)+"/'><div>"+str(j)+"</div></a> "

        fh_top = open("top_index.html", "r").read()
        fh_btm = open("bottom_index.html", "r").read()
        fh     = fh_top + serve_data +fh_btm
        return fh