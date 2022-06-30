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
            for K in k:
                if K[-1]=='n' and K[-2]=='\\':
                    lst.append(K[0:-2])
                else:
                    lst.append(K)
                
        
    