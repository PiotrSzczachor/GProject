class Assignment:
    def __init__(self, var_name, value, parent):
        self.var_name = var_name
        self.value = value
        self.parent = parent

    def __str__(self):
        return str(self.var_name) + " = " + str(self.value) + ";\n"

