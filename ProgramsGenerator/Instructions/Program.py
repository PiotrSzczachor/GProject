class Program:
    instructions = []

    def __str__(self):
        return "program\n{\n" + self.stringify_instructions() + "}"

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def stringify_instructions(self):
        instructions = ""
        for instruction in self.instructions:
            instructions += str(instruction)
        return instructions
