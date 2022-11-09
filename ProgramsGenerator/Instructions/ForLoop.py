class ForLoop:

    def __init__(self, iterator_name, start, end, increment_value):
        self.iterator_name = iterator_name
        self.start = start
        self.end = end
        self.increment_value = increment_value
        self.instructions = []

    def __str__(self):
        instructions = self.stringify_instructions()
        return "dla(int " + str(self.iterator_name) + " = " + str(self.start) + "; " + str(self.iterator_name) + " < " + str(self.end) + "; " + str(self.iterator_name) + " = " + str(self.iterator_name) + " + " + str(self.increment_value) + ")" + "\n{\n" + instructions + "}\n"

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def stringify_instructions(self):
        instructions = ""
        for instruction in self.instructions:
            instructions += str(instruction)
        return instructions

