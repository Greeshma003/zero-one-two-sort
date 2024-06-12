'''zero one two sort'''
l=[1,1,2,2,2,3]  
size=len(l)
count=0
one=0
two=0
for i in range(0,size):
    if(l[i]==1):
        count=count+1
    elif(l[i]==2):
        one=one+1
    else:
        two=two+1
print(count)
print(one)
print(two)
j=0
while count>0:
    l[j]=0
    j=j+1 
    count=count-1
while one>0:
    l[j]=1
    j=j+1 
    one=one-1
while two>0:
    l[j]=2
    j=j+1 
    two=two-1
print(l)
    
        
         