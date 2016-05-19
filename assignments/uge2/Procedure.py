import os
import sys

class BuildBlock:
    def show_in_menu():
        Button = '<div style="float: left">ProcName ( </div>' \
                 '<div class="contain">Expr</div>' \
                 '<div style="float: left"> )</div>'
        return Button

    def show_in_screen():
        Screen = '<div class = pluscontainer style="display: inline-block; min-width: 20px;">'\
                 '<div class = procedure style="display:inline-block";><input type="text" class="procname" style="float: left">' \
                 '<div style="float: left">( </div>' \
                 '<div class="contain" id="procedure" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '<div style="float: left"> )</div>' \
                 '</div><br>' \
                 '<div class="lines" id="procedure" ondrop="dropLines(event)" ondragover="allowDrop(event)"></div>' \
                 '</div>'
        return Screen