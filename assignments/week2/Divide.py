class BuildBlock:
    def show_in_menu():
        Button = '<div class="contain">Expr</div>' \
                 '<div style="float: left"> / </div>' \
                 '<div class="contain">Expr</div>'
        return Button

    def show_in_screen():
        Screen = '<div class = divide style="display: inline-block; min-width: 20px; max-height: 50px;">' \
                 '<div class="contain" id="divide" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '<div style="float: left"> / </div>' \
                 '<div class="contain" id="divide" ondrop="drop(event)" ondragover="allowDrop(event)"></div>' \
                 '</div>'
        return Screen

    def Add_Evaluation():
        Evaluation = "case 'divide': result = parseFloat(evaluate(Parent.children[0])) / parseFloat(evaluate(Parent.children[2]));\n break;"
        return Evaluation