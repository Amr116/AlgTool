import os 
import sys
from Options import Options
class BbManager:
    html_code = []

    def Validation(filepath)
        if os.path.exists(Options.root_blocks +filepath ):
            files = os.listdir(Options.root_blocks + filepath)
            return files
        else:
            # if the path does not exists then we return index.html file as front page
            return Options.root_dir + "/index.html"
        
    def start(self, filepath ):
        if os.path.exists(Options.root_blocks + filepath):
            files = os.listdir(Options.root_blocks + filepath)
            for sysfile in files:
                import sysfile
                html_code.append(sysfile.show_in_menu())

 

