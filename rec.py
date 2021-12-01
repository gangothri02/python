n=int(input())
i=0
c=0
while n!=0:
    d=n%10
    n=n//10
    if d%2:
        i+=1
    else:
        c+=1
print(i,c)
    



