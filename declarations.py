#Control Signals
Branch = 0
MemRead = 0
MemtoReg = 0
ALUOp = 0
MemWrite = 0
ALUSrc = 0

#Register File inputs and Outputs
RegWrite = 0
ReadData1 = 0
ReadData2 = 0
ReadRegister1 = 0
ReadRegister2 = 0
WriteRegister = 0
WriteDataRegFile = 0

#Immediate Generation
ImmGenOutput = 0

#ALU Control
ALUControl = 0

#PC
PC = 0

#Instruction Memory
ReadAddress = 0
Instruction = '0' * 32

#ALU output
Zero = 0
ALUResult = 0

#Data Memory
Address = 0
WriteData = 0
ReadData = 0

#Registers
x0 = 0
x1 = 0
x2 = 2147483632
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
x11 = 0
x12 = 0
x13 = 0
x14 = 0
x15 = 0
x16 = 0
x17 = 0
x18 = 0
x19 = 0
x20 = 0
x21 = 0
x22 = 0
x23 = 0
x24 = 0
x25 = 0
x26 = 0
x27 = 0
x28 = 0
x29 = 0
x30 = 0
x31 = 0
#clock
clock = 0

#TempMem
TempMem = {}
fp = open("1.mc", "r+")
for line in fp:
    inst = line.split(' ')
    a = int(inst[0], 16)
    b = int(inst[1], 16)
    TempMem[a] = b#Control Signals
Branch = 0
MemRead = 0
MemtoReg = 0
ALUOp = 0
MemWrite = 0
ALUSrc = 0

#Register File inputs and Outputs
RegWrite = 0
ReadData1 = 0
ReadData2 = 0
ReadRegister1 = 0
ReadRegister2 = 0
WriteRegister = 0
WriteDataRegFile = 0

#Immediate Generation
ImmGenOutput = 0

#ALU Control
ALUControl = 0

#PC
PC = 0

#Instruction Memory
ReadAddress = 0
Instruction = '0' * 32

#ALU output
Zero = 0
ALUResult = 0

#Data Memory
Address = 0
WriteData = 0
ReadData = 0

#Registers
x0 = 0
x1 = 0
x2 = 2147483632
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
x11 = 0
x12 = 0
x13 = 0
x14 = 0
x15 = 0
x16 = 0
x17 = 0
x18 = 0
x19 = 0
x20 = 0
x21 = 0
x22 = 0
x23 = 0
x24 = 0
x25 = 0
x26 = 0
x27 = 0
x28 = 0
x29 = 0
x30 = 0
x31 = 0
#clock
clock = 0

#TempMem
TempMem = {}
def initialize_mem():
    fp = open("1.mc", "r+")
    for line in fp:
        inst = line.split(' ')
        a = int(inst[0], 16)
        b = inst[1][1:]
        if(len(b)==8):
            TempMem[a] = b[6:]
            TempMem[a+1] = b[4:6]
            TempMem[a+2] = b[2:4]
            TempMem[a+3] = b[0:2]
        elif(len(b)==4):
            TempMem[a] = b[2:]
            TempMem[a+1] = b[0:2]
        else:
            TempMem[a] = b