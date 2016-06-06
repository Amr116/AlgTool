import os
import sys

class BuildBlock:
    def show_in_menu():
        Button = '<div style="float: left">return </div>' \
                 '<div class="contain">Expr</div>'
        return Button

    def show_in_screen():
        Screen = '<div class = pluscontainer style="display: inline-block; min-width: 20px; max-height: 50px;">' \
                 '<div style="float: left">return </div>' \
                 '<div class="contain" id="return" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '</div>'
        return Screen

    def Add_Evaluation():
        return ''