import os

class Options:
    cwd      = os.getcwd()
    dc       = cwd.split("/")[-1]
    root_dir = cwd.replace(dc, "")

#    root_dir   = os.getcwd()
#    root_dir   = "/home/amr/Desktop/AlgTool"
#    server_dir = "/home/amr/Desktop/AlgTool/webserver"
