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

    def serve_media(self, content, csock):
        Response.reply_200(csock, content)

    def serve_index(self, csock):
        fd = "assignments"
        data = os.listdir(fd)
        data_list = []
        serve_data= ""
        for i in data:
            data_list.append(fd + '/' + str(i))

        for j in data_list:
            serve_data += "<a class='btn btn-success week' href='/"+str(j)+"/'><div>"+str(j.replace("/","-"))+"</div></a> "
 
        fh_top = open("template/top_index.html", "r").read()
        fh_btm = open("template/bottom_index.html", "r").read()
        fh     = fh_top + serve_data +fh_btm

        Response.reply_200(csock, fh)
        #return fh
