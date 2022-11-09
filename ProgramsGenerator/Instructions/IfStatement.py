class IfStatement:

    def __init__(self, value1, comparator, value2):
        self.value1 = value1
        self.value2 = value2
        self.comparator = comparator
        self.instructions = []

    def __str__(self):
        instructions = self.stringify_instructions()
        return "jezeli(" + str(self.value1) + " " + self.comparator + " " + str(self.value2) + ")\n{\n" + instructions + "}\n"

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def stringify_instructions(self):
        instructions = ""
        for instruction in self.instructions:
            instructions += str(instruction)
        return instructions
