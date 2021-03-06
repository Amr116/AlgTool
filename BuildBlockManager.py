import os, os.path
import importlib
import sys
from Options import Options
class BbManager:

   def start(filepath):
        BuildBlockButton = ""
        AllCase = ""
        Evaluation = ""
        if os.path.exists(filepath):#Options.root_blocks + filepath):
            files = os.listdir(filepath)#Options.root_blocks + filepath)
            for sysfile in files:
                if sysfile.endswith(".py"):
                    path = os.path.join(filepath,sysfile)
                    id = sysfile[:-3]
                    #print(id)
                    path = path.replace("/",".")[:-3]
                    sy = importlib.import_module(path)
                    Button = '<div class="blocks" id="' + id + '" draggable="true" style="display: inline-block; border: 1px solid black;" ondragstart="drag(event)">' + \
                           sy.BuildBlock.show_in_menu() + "</div>\n"
                    BuildBlockButton += Button
                    Screen = "case '" + id + "': str = '" + sy.BuildBlock.show_in_screen() + "';\n break;\n"
                    AllCase += Screen
                    Evaluation += sy.BuildBlock.Add_Evaluation()
        else:
            print("ELSE")

        BuildBlockScreen = 'function insert(id){\n switch (id) {\n' + AllCase + '}\n return str;\n}\n\n'
        Evaluation_Function = 'function evaluate(child) {\n var Parent = child.children[0];\n ' \
                              'var Class = Parent.className;\n switch (Class) {\n' + Evaluation + '}\n return result;\n}\n\n'

        return BuildBlockButton, BuildBlockScreen, Evaluation_Function

