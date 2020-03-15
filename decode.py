from declarations import *
from bitstring import BitArray
def decode():
    if(Instruction == '0' * 32):
        exit_routine()
    else:
        Instruction1 = Instruction[::-1]
        opcode = Instruction1[0:8]
        ReadRegister1 = int(Instruction1[15:20], 2)
        ReadRegister2 = int(Instruction1[20:25], 2)
        WriteRegister = int(Instruction1[7:12], 2)
        if(opcode == '0000011' or opcode == '0010011' or opcode == '1100111'):
            ImmGenOutput = BitArray(Instruction1[20:]).int
            ALUSrc2 = 1
            ALUSrc1 = 0
        elif(opcode == '0100011'):
            ImmGenOutput = BitArray(Instruction1[7:12]+Instruction1[25:]).int
            ALUSrc2 = 1
            ALUSrc1 = 0
        elif(opcode == '1100011'):
            ImmGenOutput = BitArray(Instruction1[8:13] + Instruction1[25:31] + Instruction1[7] + Instruction1[31]).int
            ALUSrc2 = 0
            ALUSrc1 = 0
        elif(opcode == '0010111' or opcode == '0110111'):
            ImmGenOutput = BitArray(Instruction1[12:]).int
            ALUSrc2 = 2
            ALUSrc1 = 1 if opcode == '0010111' else 2
        elif(opcode == '1101111'):
            ImmGenOutput = BitArray(Instruction1[21:31]+Instruction1[20]+Instruction1[12:20]+Instruction1[31]).int
            ALUSrc2 = 0
            ALUSrc1 = 0
        else:
            ALUSrc2 = 0
            ALUSrc1 = 0
        if(opcode == '1100011'):
            Branch = int(Instruction1[12:15],2) + 1
        else:
            Branch = 0
        PCReg = 1 if opcode == '1100111' else 0
        MemRead = 1 if opcode == '0000011' else 0
        MemWrite = 1 if opcode == '0100011' else 0
        RegWrite = 0 if opcode == '0100011' or  opcode == '1100011' else 1
        func3 = Instruction1[12:15]
        func7 = Instruction1[25:]
        if opcode == 