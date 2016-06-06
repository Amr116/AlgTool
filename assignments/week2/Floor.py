import os
import sys

class BuildBlock:
    def show_in_menu():
        Button = '<div style="float: left">|_ </div>' \
                 '<div class="contain">Expr</div>' \
                 '<div style="float: left"> _|</div>'
        return Button

    def show_in_screen():
        Screen = '<div class = floor style="display: inline-block; min-width: 20px; max-height: 50px;">' \
                 '<div style="float: left">|_ </div>' \
                 '<div class="contain" id="floor" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '<div style="float: left"> _|</div>' \
                 '</div>'
        return Screen

    def Add_Evaluation():
        Evaluation = "case 'floor': result = Math.floor(evaluate(Parent.children[1]));\n break;"
        return Evaluation