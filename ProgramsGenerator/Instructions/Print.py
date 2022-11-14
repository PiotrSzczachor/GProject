class Print:
    def __init__(self, variable, parent):
        self.variable = variable
        self.parent = parent

    def __str__(self):
        return "wyswietl(" + str(self.variable) + ");\n"
