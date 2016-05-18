import os
import sys

class BuildBlock:
    def show_in_menu():
        Button = '<div style="float: left">ProcName ( </div>' \
                 '<div class="contain">Expr</div>' \
                 '<div style="float: left"> )</div>'
        return Button

    def show_in_screen():
        Screen = '<div class = procedure style="float: left"><input type="text" class="procname">' \
                 '<div style="float: left">( </div>' \
                 '<div class="contain" id="procedure" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '<div style="float: left"> )</div>' \
                 '</div>' \
                 '<div class="contain" id="procedure" ondrop="dropLines(event)" ondragover="allowDrop(event)"></div>'
        return Screen