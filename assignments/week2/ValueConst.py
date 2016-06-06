class BuildBlock:
    def show_in_menu():
        Button = '<div class="contain">Constant</div>'
        return Button

    def show_in_screen():
        Screen = '<input type="number" class="constant" id="valueconst" style="width: 50px"/>'
        return Screen

    def Add_Evaluation():
        Evaluation = "case 'constant': result = Parent.value;\n break;"
        return Evaluation