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
        BuildBlockButton = ""
        BuildBlockScreen = ""
        if os.path.exists(filepath):#Options.root_blocks + filepath):
            files = os.listdir(filepath)#Options.root_blocks + filepath)
            for sysfile in files:
                if sysfile.endswith(".py"):
                    path = os.path.join(filepath,sysfile)
                    id = sysfile[:-3]
                    print(id)
                    path = path.replace("/",".")[:-3]
                    sy = importlib.import_module(path)
                    Button = '<div id="' + id + '" draggable="true" style="display: inline-block; border: 1px solid black;" ondragstart="drag(event)">' + \
                           sy.BuildBlock.show_in_menu() + "</div>\n<br>"
                    BuildBlockButton += Button
                    Screen = "case '" + id + "': str = '" + \
                           sy.BuildBlock.show_in_screen() + "';\n break;\n"
                    BuildBlockScreen += Screen

        else:
            print("ELSE")

        return BuildBlockButton, BuildBlockScreen
#if __name__ == '__main__':
#    manager = BbManager()
#    ls = manager.start("assignments/uge1/")
#    print("=============" + ls)
