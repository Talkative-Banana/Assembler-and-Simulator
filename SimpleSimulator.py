
memory = []
Instruction = []

pointer = [0,0,0,0,0,0,0,0]
R0      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R1      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R2      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R3      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R4      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R5      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
R6      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
FLAGS   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Op_Code_Dict = {'10000':'add','10001':'sub','10010':'mov_Im','10011':'mov_Reg',
                '10100':'ld','10101':'st','10110':'mul','10111':'div','11000':'rs',
                '11001':'ls','11010':'xor','11011':'or','11100':'and','11101':'not',
                '11110':'cmp','11111':'jmp','01100':'jlt','01101':'jgt','01111':'je','01010':'hlt'}

Register_Dict = {'000':R0,'001':R1,'010':R2,'011':R3,'100':R4,'101':R5,'110':R6,'111':FLAGS}
# Register_Dict_ = {'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}

def lst_val(a,b):
    k = 0
    for i in range(0,len(a)):
        k += int(a[i]) * (2 **(b-i-1))
    return k


# Memory Creation
def Create_Memory():
    le = len(memory)
    for i in range(256-le):
        memory.append('0000000000000000')

# Program Counter 
def Program_Counter():
    for i in pointer:
        print(i,end = '')
    print(end=' ')

# Register Value
def Register_Value(Rx):
    if Rx=='FLAGS':
        for i in Rx:
            print(i,end='')
        print(end =' ')
    else:
        for i in Rx:
            print(i,end='')
        

# Memory Value
def Memory(a):
    print(memory[a])

def Execution_Engine():
    a = int(pointer,10)
    b = memory(a)
    
def Op_Code(a):
    Op = a[:5]
    return Op_Code_Dict[Op]

def Flag_Clear():
    for i in range(1,5):
        FLAGS[-i] = 0

def Output():
    arr = []
    arr.extend(pointer)
    arr.append(' ')
    arr.extend(R0)
    arr.append(' ')
    arr.extend(R1)
    arr.append(' ')
    arr.extend(R2)
    arr.append(' ')
    arr.extend(R3)
    arr.append(' ')
    arr.extend(R4)
    arr.append(' ')
    arr.extend(R5)
    arr.append(' ')
    arr.extend(R6)
    arr.append(' ')
    arr.extend(FLAGS)
    for i in arr:
        print (i,end='',sep=' ')
    print(end ='\n')


def Memory_Out():
    for i in range(256):
        print(memory[i])
        

def change(a,b,c):
    lst = []
    lst.extend(a)
    lst[-b] = f'{c}'
    for i in lst:
        a = ''+ f'{i}'

def bin_add(a,b,c,d,e):
    b = int(b)
    c = int(c)
    if(c+b+d == 0):
        change(a,-e,'0')
        return 0
    elif(c+b+d == 2):
        change(a,-e,'0')
        return 1
    else:
        change(a,-e,'1')
        return 0

def bin_sub(a,b,c,d,e):
    b=int(b)
    c=int(c)
    if(b+d-c == 0):
        change(a,-e,'0')
        return 0
    elif(b+d-c == 1):
        change(a,-e,'1')
        return 0
    elif(b+d-c == -1):
        change(a,-e,'1')
        return 1

# Cmp
def cmp(Rx,Ry,k):
    a = lst_val(Rx,16)
    b = lst_val(Ry,16)
    if(a-b>0):
        if(k):
            FLAGS[-2] = 1
        return 1
    elif(a-b<0):
        if(k):
            FLAGS[-3] = 1
        # change(FLAGS,3,'1')
        return 0
    elif(a == b):
        # change(FLAGS,1,'1')
        if(k):
            FLAGS[-1] = 1
        return 1

# Add
def add(Rx,Ry,Rz):
    a =lst_val(Rx,16) 
    b =lst_val(Ry,16) 
    if (a + b >65535):
        FLAGS[-4] = 1
    else:
        p=bin(a+b)[2:]
        k =str(p)
        le = len(p) 
        z = '0'*(16-le) + k
        for i in range(16):
            Rz[i] = z[i]
    
# Sub
def sub(Rx,Ry,Rz):
    if(cmp(Rx,Ry,0) == 0):
        change(FLAGS,4,'1')
        # FLAGS[-4] = 1
        for i in range(16):
            Rz[i] = 0 
        return 
    else:
        a =lst_val(Rx,16)
        b =lst_val(Ry,16)
        p=bin(a-b)[2:]
        k =str(p)
        le = len(p) 
        z = '0'*(16-le) + k
        for i in range(16):
            Rz[i] = z[i] 
        return

# Mov_Imm
def mov_Imm(Rx,a):
    s = '00000000' + a
    for i in range(len(Rx)):
        Rx[i] = s[i] 

# Mov_Reg
def mov_reg(Rx,Ry):
    for i in range(0,16):
        # change(Ry,-i,Rx[i])
        Ry[i] = Rx[i]
    return

# Load_Reg
def ld(Rx,a):
    a = int(a,2) 
    for i in range(16):
        Rx[i] = memory[a][i]
    return 

# Store_Reg
def st(Rx,b):
    s =''
    for i in Rx:
        s = s + i
        memory[int(b,2)] = s
    return

# Multiply
def mul(Rx,Ry,Rz):
    Rz = '0000000000000000'
    a = lst_val(Rx,16)
    b = lst_val(Ry,16)
    if(a*b> 65535):
        FLAGS[-4] = 1
        # change(FLAGS,4,'1')
    else:
        s = str(bin(a*b))
        k = len(s)
        r = '0'*(8-k) + s
        for i in range(16):
            Rz[i] = r[i]
    return Rz

# Divide
def div(Rx,Ry):
    a = lst_val(Rx)
    b = lst_val(Ry)
    s = bin(a//b)
    t = bin(a%b)
    k = len(s)
    e = len(t)
    r = '0'*(8-k) + s
    n = '0'*(8-e) + t
    for i in range(16):
        R0[i] = r[i]
        R1[i] = n[i]

# R_shift
def R_shift(Rx,a):
    s = int(a,2)
    for i in range(len(Rx)):
        Rx[(s+i)%16] = Rx[i]
    for i in range(s):
        Rx[i] = 0
    return

# L_shift
def L_shift(Rx,a):
    s = int(a,2)
    for i in range(len(Rx)):
        Rx[i] = Rx[(s+i)%16]
    for i in range(s):
        Rx[-i] = 0
    return

# Xor
def Xor(Rx,Ry,Rz):
    for i in range(16):
        a = int(Rx[i])
        b = int(Ry[i])
        Rz[i] = str((a*(1-b)+b*(1-a))%2)

# Or
def Or(Rx,Ry,Rz):
    for i in range(16):
        a = int(Rx[i])
        b = int(Ry[i])
        Rz[i] = ((a+b)%2)

# And
def And(Rx,Ry,Rz):
    for i in range(16):
        a = int(Rx[i])
        b = int(Ry[i])
        Rz[i] = (a*b)

# Invert
def Invert(Rx,Ry):
    for i in range(16):
        a = int(Rx[i])
        Ry[i] = (1-a) 

# Unconditional Jump
def jmp(a):
    for i in range(8):
        pointer[i] = a[i]
    

# Jump if less than 
def jlt(a):
    if(FLAGS[-3] == 1):
        for i in range(8):
            pointer[i] = a[i]
        Flag_Clear()
        Output()
    else:
        Flag_Clear()
        Output()
        Update_pointer(pointer,1)
        
# Jump if greater than
def jgt(a):
    if(FLAGS[-2] == 1):
        for i in range(8):
            pointer[i] = a[i]
        Flag_Clear()
        Output()
        # print(a)
    else:
        Flag_Clear()
        Output()
        Update_pointer(pointer,1)

# Jump if Equal
def je(a):
    if(FLAGS[-1] == 1):
        for i in range(8):
            pointer[i] = a[i]
        Flag_Clear()
        Output()
    else:
        Flag_Clear()
        Output()
        Update_pointer(pointer,1)

# Update Pointer
def Update_pointer(pointer,p):
    r = lst_val(pointer,8)
    if(r>=255):
        return
    t = bin((p + r))[2:]
    k = str(t)
    le = len(k)
    s = '0'*(8-le) + t
    for i in range(len(s)):
        pointer[i] = int (s[i])
    
# Input
for i in range(256):
    try:
        In = str(input())
        Instruction.append(In)
        memory.append(In)
    except:
        break

Create_Memory()
halted = False

while(halted == False):
    
    # Loop Terminating Condition
    Inst = lst_val(pointer,8)
    
    if(Op_Code(Instruction[Inst]) == 'hlt'):
        halted =True
        Output()
        break
  
    elif(Op_Code(Instruction[Inst]) == 'add'):
        add(Register_Dict[(Instruction[Inst])[7:10]],Register_Dict[(Instruction[Inst])[10:13]],Register_Dict[(Instruction[Inst])[13:16]])
        Output()
        Update_pointer(pointer,1)
    
    elif(Op_Code(Instruction[Inst]) == 'sub'):
        sub(Register_Dict[Instruction[Inst][7:10]],Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)
    
    elif(Op_Code(Instruction[Inst]) == 'mov_Im'):
        mov_Imm(Register_Dict[Instruction[Inst][5:8]],Instruction[Inst][8:16])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'mov_Reg'):
        mov_reg(Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'ld'):
        ld(Register_Dict[Instruction[Inst][5:8]],Instruction[Inst][8:16])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'st'):
        st(Register_Dict[Instruction[Inst][5:8]],Instruction[Inst][8:16])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'mul'):
        mul(Register_Dict[Instruction[Inst][8:10]],Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'div'):
        div(Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'rs'):
        R_shift(Register_Dict[Instruction[Inst][5:8]],Instruction[Inst][8:16])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'ls'):
        L_shift(Register_Dict[Instruction[Inst][5:8]],Instruction[Inst][8:16])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'xor'):
        Xor(Register_Dict[Instruction[Inst][7:10]],Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'or'):
        Or(Register_Dict[Instruction[Inst][7:10]],Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'and'):
        And(Register_Dict[Instruction[Inst][7:10]],Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'not'):
        Invert(Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]])
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'cmp'):
        cmp(Register_Dict[Instruction[Inst][10:13]],Register_Dict[Instruction[Inst][13:16]],1)
        Output()
        Update_pointer(pointer,1)

    elif(Op_Code(Instruction[Inst]) == 'jmp'):
        Output()
        Flag_Clear()
        jmp(Instruction[Inst][8:16])
        continue

    elif(Op_Code(Instruction[Inst]) == 'jgt'):
        jgt(Instruction[Inst][8:16])
        # Flag_Clear()
        # Output()
        continue

    elif(Op_Code(Instruction[Inst]) == 'jlt'):
        jlt(Instruction[Inst][8:16])
        # Flag_Clear()
        # Output()
        continue

    elif(Op_Code(Instruction[Inst]) == 'je'):
        je(Instruction[Inst][8:16])
        # Flag_Clear()
        # Output()
        continue

Memory_Out()