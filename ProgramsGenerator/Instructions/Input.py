class Input:
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return "wprowadz(" + str(self.variable) + ");\n"
