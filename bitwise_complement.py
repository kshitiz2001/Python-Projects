n=map(int,input().split(" "))
l=list(n)
sum1=0
c=0
for i in range (len(l)):
    c=-(l[i]+1)
    sum1=sum1+c
if sum1%10 == 0:
    print("YES")
else:
    print("NO")
