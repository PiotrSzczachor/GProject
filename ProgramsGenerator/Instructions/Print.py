class Print:
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return "wyswietl(" + str(self.variable) + ");\n"
