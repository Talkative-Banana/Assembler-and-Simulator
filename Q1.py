#Reading the file
a=open("Text.txt",'r')
for i in a:
    if(i==''):
        pass
    else:
        b=a.readline()
        lst=[]
        for j in b:
            k=b.split(' ')
            for K in k:# Registers
reg = {'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS`':'111'}

# OpCodes
op_code = {"add" : "10000" ,"sub" : "10001","mov_imm" : "10010" ,
"mov_reg" : "10011", "ld" :"10100","st" : "10101","mul" : "10110",
"div" : "10111","rs" : "11000",
"ls" : "11001" ,"xor" : "11010","or" : "11011","and" : "11100" 
,"not" :"11101","cmp" : "11110","jmp" : "11111", "jlt" : "01100",
 "jgt" : "01101", "je" : "01111", "hlt" : "01010"}
#Addition

# Single bit addition 
def add(x,y,reg_z,carry):
    reg_z=x+y+carry
    if(reg_z==2):
        reg_z=0
        carry=1
    elif(reg_z==3):
        reg_z=1
        carry=1
    elif(reg_z==1):
        reg_z=1
        carry=0
    else:
        reg_z=0
        carry=0
    return carry

#Register Addition
def addition(reg_x,reg_y,reg_z):
    i=15
    carry=0
    flag=0
    while(i>=0):
        if(i==15):
            carry=add(reg_x[i],reg_y[i],reg_z[i],0)
        elif(i==0):
            carry=add(reg_x[i],reg_y[i],reg_z[i],carry)
            if carry==1:
                flag=1
                return flag
            return flag
        else:
            carry=add(reg_x[i],reg_y[i],reg_z[i],carry)
# Decimal to binary

def Radix_A_to_B(a,b,r):
    conv={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    conv_rev={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    # n=str(input('enter number:')).upper()
    dec=0
    p=len(str(r))-1
    for i in str(r):
        dec += conv[i]*a**p
        p-=1
    emp_str=''
    while (dec!=0):
        rem=dec%b
        emp_str += conv_rev[rem]
        dec=dec//b

    emp_str_fin=emp_str[::-1]            

    return emp_str_fin

#Reading the file
print(Radix_A_to_B(10,2,16))
inp=open("Text.txt",'r')
out=open("Output.txt",'a+')
for i in inp:
    Str=''
    if(i==''):
        pass
    else:
        lst=[]
        for j in i:
            k=i.split(' ')
            for K in k:
                if K[-1]=='n' and K[-2]=='\\':
                    lst.append(K[0:-2])
                else:
                    lst.append(K)
        # print(lst[0])
        for key in op_code.keys():
            if(key==lst[0]):
                Str=''+op_code[key]
                for Key in reg.keys():
                    if(Key==lst[1]):
                        Str=Str+reg[Key]
                print(Str)
            elif(lst[0]=='mov'):
                if(lst[2][0]=='$'):
                    Str=''+op_code['mov_imm']
                    for Key in reg.keys():
                        if(Key==lst[1]):
                            Str=Str+reg[Key]
                    val=str(Radix_A_to_B(10,2,int(lst[2][1:])))
                    le=len(val)
                    if(le==8):
                        pass
                    else:
                        u=8-le
                    Str=Str+u*'0'+val
                    print(Str)
                else:
                    Str=''+op_code['mov_reg']
                    for Key in reg.keys():
                        if(Key==lst[1]):
                            Str=Str+reg[Key]
                            print(Str)
                    # val=lst[2][1:]
                    val=Radix_A_to_B(10,2,lst[2][1:])
            # elif(lst[0]==):
# def subtract():
                if K[-1]=='n' and K[-2]=='\\':
                    lst.append(K[0:-2])
                else:
                    lst.append(K)
                   
                
        
    
