inp=input()
max=0
i=1
lst=[]
while(len(inp)!=0):
    x=(inp[:i*2])
    # print(x)
    lst.append((x.split()))
    inp=inp[i*2:]
    # print(inp)
    i=i+1
max=[0]*len(lst) 
position=[0]*len(lst) 
for i in range(len(lst)):
    if(i==0):
        max[i]=int(lst[i][0])
        position[i]=0
        continue
    if(int(lst[i][position[i-1]]) > int(lst[i][position[i-1]+1])):
        max[i]=max[i-1]+int(lst[i][position[i-1]])
        position[i]=position[i-1]
    else:
        max[i]=max[i-1]+int(lst[i][position[i-1]+1])
        position[i]=position[i-1]+1
    # print(position[i])
print(max[i])
