import re
from common_backend import *

label_instructions = ['jal', 'beq']

def parse(line, num):
    label = re.compile("(\A\w+)\:")
    label_matches = label.search(line)

    instruction = re.compile("((\w)+\s)+")
    instruction_matches = instruction.search(line)

    data = re.compile("\.(\w+)")
    data_matches = data.search(line)

    if(label_matches != None):
        label_dict[label_matches.group(1)] = 4*num

    if(instruction_matches != None):
        if()

    print(label_dict)

parse("addi x2 x4 123", 2)
parse("abc:", 14)
parse(".word", 1)
