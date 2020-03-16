import re
from common_backend import *

def parse(line):
    label = re.compile("\A\w+\:")
    label_matches = label.search(line)

    instruction = re.compile("((\w)+\s)+")
    instruction_matches = instruction.search(line)

    data = re.compile("\.(\w+)")
    data_matches = data.search(line)

    print(label_matches)
    print(instruction_matches)

parse("addi x2 x4 123")
parse("abc:")
