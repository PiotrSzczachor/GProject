class VarDeclaration:
    def __init__(self, type_, var, value, parent):
        self.type = type_
        self.var = var
        self.value = value
        self.parent = parent

    def __str__(self):
        return str(self.type) + " " + str(self.var) + " = " + str(self.value) + ";\n"