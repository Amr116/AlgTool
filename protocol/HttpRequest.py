from Options import Options
from filesystem.Filesystem import Filesystem
from protocol.Response import Response


class HttpRequest:

    def serve_file(self, filepath, filename, csock):
        exists = Filesystem.file_exists(filepath, filename)
        if exists:
            # remember to call BbManager to gernerate the blocks inside index.html file
            # before serving
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
