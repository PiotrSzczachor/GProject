class Input:
    def __init__(self, variable, parent):
        self.variable = variable
        self.parent = parent

    def __str__(self):
        return "wprowadz(" + str(self.variable) + ");\n"
