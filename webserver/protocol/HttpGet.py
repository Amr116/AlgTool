import os

from Options import Options
from filesystem.Filesystem import Filesystem
from protocol.Response import Response
from protocol.HttpRequest import HttpRequest


class HttpGet(HttpRequest):

    def __init__(self, match, csock):
	"""
        filepath = match.group(2)
        filename = match.group(3)
	"""
	filename = match.split("/")[-1]
	filepath = match.replace(filename,"")
	print("File name : "+filename)
	print("File path : "+filepath)

	if filepath is not None and (filepath is "/uge1" or filepath is "/uge2" or filepath is "/uge3" or filepath is "/uge4" or filepath is "/uge5"):
	    filepath = "assignments"+filepath
	else:
	    filepath = "/"


	if filename is not None and filename is "index.html":
	    filename = filename
	else:
	    filename = "index.html"


	# Check if project main page "index.html" exists in the project directory
        if Filesystem.file_exists(filepath, filename):  
            self.serve_file(filepath, filename, csock)
	# if there is no index.html file, so we serve Not Found error message
        else:  
	        Response.reply_404(csock)

