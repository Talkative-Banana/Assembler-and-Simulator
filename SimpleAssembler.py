# Registers
reg = {'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

# OpCodes
op_code = {"add" : "10000" ,"sub" : "10001","mov_imm" : "10010" ,
"mov_reg" : "10011", "ld" :"10100","st" : "10101","mul" : "10110",
"div" : "10111","rs" : "11000",
"ls" : "11001" ,"xor" : "11010","or" : "11011","and" : "11100" 
,"not" :"11101","cmp" : "11110","jmp" : "11111", "jlt" : "01100",
 "jgt" : "01101", "je" : "01111", "hlt" : "01010"}

def check_label(lst,count):
    if lst[0][-1]==':':
        C=Radix_A_to_B(10,2,count)
        if(len(C)==8):
            pass
        else:
            r=8-len(C)
            C='0'*(8-r)+C
        labels_reg[lst[0]]=C
        return 1
    return 0

var_reg={}
labels_reg={}

def var(key,value):
    var_reg[key]=value

def Type_A_Ins(lst,count):

    Type_A=['add','sub','mul','xor','or','and']
    # print(lst[0])
    if lst[0] in Type_A:
        Str=''+op_code[lst[0]]
        STR=''
        for ii in range(1,4):
            if lst[ii][:2] in reg.keys():
                STR=STR+reg[lst[ii][:2]]
            elif lst[ii][:5]=='FLAGS':
                STR=STR+reg[lst[ii][:5]]
            else:
                print(f"Error (Invalid Register Name on line {count})")
                exit()
                return ''
        Len=len(STR)
        if(Len==14):
            nz=0
        else:
            nz=11-Len
        Str=Str+'0'*nz
        Str=Str+STR
        # print(Str)
        return Str
    return 'NULL'

def Type_B_Ins(lst,count):

    Type_B=['mov','ls','rs']
    if lst[0] in Type_B:
        if(lst[0]=='mov' and lst[2][0]=='$'):
            Str=''+op_code['mov_imm']
            if lst[1][:2] in reg.keys():
                    Str=Str+reg[lst[1][:2]]
            elif lst[1][:5]=='FLAGS':
                    Str=Str+reg[lst[1][:5]]
            else:
                print(f"Error (Invalid Register Name on line {count})")
                exit()
                return ''
            val=str(Radix_A_to_B(10,2,int(lst[2][1:])))
            le=len(val)
            if(le==8):
                pass
            else:
                u=8-le
            Str=Str+u*'0'
            Str=Str+val
        else:
            Str=''+op_code['ls']
            if lst[1][:2] in reg.keys():
                Str=Str+reg[lst[1][:2]]
            elif lst[1][:5]=='FLAGS':
                Str=Str+reg[lst[1][:5]]
            else:
                print(f"Error (Invalid Register Name on line {count})")
                exit()
                return ''
            val=str(Radix_A_to_B(10,2,int(lst[2][1:])))
            le=len(val)
            if(le==8):
                pass
            else:
                u=8-le
            Str=Str+u*'0'
            Str=Str+val
        return Str
    return 'NULL'

def Type_C_Ins(lst,count):
    Type_C=['mov','div','not','cmp']
    if lst[0] in Type_C:
        if lst[0]=='mov':
            Str=''+op_code['mov_reg']
            STR=''
            for ii in range(1,3):
                if lst[ii][:2] in reg.keys():
                    STR=STR+reg[lst[ii][:2]]
                elif lst[1][:5]=='FLAGS':
                    STR=STR+reg[lst[ii][:5]]
                else:
                    print(f"Error (Invalid Register Name on line {count})")
                    exit()
                    return
            Len=len(STR)
            if(Len==14):
                nz=0
            else:
                nz=11-Len
            Str=Str+'0'*nz
            Str=Str+STR
        
        else:
            Str=''+op_code[lst[0]]
            STR=''
            for ii in range(1,3):
                if lst[ii][:2] in reg.keys():
                        STR=STR+reg[lst[ii][:2]]
                elif lst[1][:5]=='FLAGS':
                        STR=STR+reg[lst[ii][:5]]
                else:
                    print(f"Error (Invalid Register Name on line {count})")
                    exit()
                    return ''
                
            Len=len(STR)
            if(Len==14):
                nz=0
            else:
                nz=11-Len
            Str=Str+'0'*nz
            Str=Str+STR
            return Str
    return 'NULL'

def Type_D_Ins(lst,count):
    Type_D=['ld','st']
    if lst[0] in Type_D:
        Str=''+op_code[lst[0]]
        if lst[1][:2] in reg.keys():
                Str=Str+reg[lst[1][:2]]
        elif lst[1][:5]=='FLAGS':
            Str=Str+reg[lst[1][:2]]
        else:
            print(f"Error (Invalid Register Name on line {count})")
            exit()
            return ''

        k=len(lst[2])
        if lst[2] in var_reg:
            Str=Str+var_reg[lst[2]]
            return Str
        else:
            print(f"Undefined register/Variable used on line {count}")
            exit()

        if(k==8):
            pass
        else:
            p=8-k
        STR='0'*p+lst[2]
        Str=Str+STR
        # k=len(Radix_A_to_B(10,2,count))
        # if(k==8):
        #     pass
        # else:
        #     p=8-k
        # STR='0'*p+str(Radix_A_to_B(10,2,count))
        # Str=Str+STR
        return Str
    return 'NULL'
        
def Type_E_Ins(lst,count):
    Type_E=['je','jgt','jlt','jmp']
    if lst[0] in Type_E:
        Str=''+op_code[lst[0]]
        Str=Str+'000'
        k=len(lst[1])

        # print(var_reg)
        if lst[1] in var_reg:
            Str=Str+var_reg[lst[1]]
            return Str
        
        else:
            print(f"Undefined register/Variable used on line {count}")
            exit()


        if(k==8):
            pass
        else:
            p=8-k
            STR='0'*p+lst[1]
            Str=Str+STR
        return Str
    return 'NULL'

def Type_F_Ins(lst):
    Type_F=['hlt']
    if lst[0] in Type_F:
        Str=''+op_code['hlt']
        Str=Str+'00000000000'
        return Str
    return 'NULL'

# Decimal to binary
def Radix_A_to_B(a,b,r):

    if isinstance(r,int):
        pass
    else:
        print("Only supports whole Number b/w [0,255]")
        return 'NULL'
    
    conv={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    conv_rev={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
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
inp=open("Text.txt",'w')
out=open("Output.txt",'w')
var_count=0
inst_count=0
Inst_count=0
hlt_count=0
for line in inp:
    if line[0:3]=='var':
        var_count+=1
    else:
        inst_count+=1
        Inst_count+=1
        if line[0:3]=='hlt':
            hlt_count+=1

# print(inst_count)
# inp=open("Text.txt",'r')
count=0
for i in inp:
    # print("HLO")  
    Str=''
    if(i==''): # Empty line
        pass

    else:
        lst=[]
        k=[]
        k=i.split()
        for K in k: 
            lst.append(K)
        # Op Code 

        # Type A (3 register Type)
        count+=1
        if check_label(lst,count)==1:
            for i in range (1,len(lst)):
                lst[i-1]=lst[i]

        else:
            pass

        if(hlt_count!=1):
            print(f'Invalid number of halt(s) {hlt_count}')
            break

        if(Type_A_Ins(lst,count)!='NULL'):
            out.write(Type_A_Ins(lst,count))  
            out.write('\n')

        # Type B (register Immediate type)
        elif(Type_B_Ins(lst,count)!='NULL'):
            out.write(Type_B_Ins(lst,count))  
            out.write('\n')

        # Type C (2 register type)
        elif(Type_C_Ins(lst,count)!='NULL'):
            out.write(Type_C_Ins(lst,count)) 
            out.write('\n')

        # Type D (register and memory address type)
        elif(Type_D_Ins(lst,count)!='NULL'):
            out.write(Type_D_Ins(lst,count))
            inst_count+=1 
            out.write('\n')

        # Type E (memory address type)
        elif(Type_E_Ins(lst,inst_count)!='NULL'):
            out.write(Type_E_Ins(lst,inst_count)) 
            out.write('\n')

        # Type F(halt)
        elif(Type_F_Ins(lst)!='NULL'):
            out.write(Type_F_Ins(lst)) 
            out.write('\n')

        elif(lst[0]=='var'):
            STR=''+Radix_A_to_B(10,2,Inst_count)
            if(len(Radix_A_to_B(10,2,Inst_count))==8):
                var(lst[1],STR)
            else:
                o=len(STR)
                STR='0'*(8-o)+STR
            var(lst[1],STR)
            Inst_count+=1
            # print("hlo")



out.close()
inp.close()

# Simulator 


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
# def subtract():

