class Assignment:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def __str__(self):
        return str(self.var_name) + " = " + str(self.value) + ";\n"

