import os, os.path
import importlib
import sys
from Options import Options
class BbManager:

    """
    def Validation(filepath)
        if os.path.exists(Options.root_blocks +filepath ):
            files = os.listdir(Options.root_blocks + filepath)
            return files
        else:
            # if the path does not exists then we return index.html file as front page
            return Options.root_dir + "/index.html"
    """
    def start(filepath):
        html_code = ""
        if os.path.exists(filepath):#Options.root_blocks + filepath):
            files = os.listdir(filepath)#Options.root_blocks + filepath)
            for sysfile in files:
                if sysfile.endswith(".py"):
                    path = os.path.join(filepath,sysfile)
                    print(path)
                    path = path.replace("/",".")[:-3]
                    sy = importlib.import_module(path)
                    html = sy.test.show_in_menu() +  "\n"
                    html_code += html
                    #print(self.html_code)

        else:
            print("ELSE")

        return html_code
#if __name__ == '__main__':
#    manager = BbManager()
#    ls = manager.start("assignments/uge1/")
#    print("=============" + ls)
