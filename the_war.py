a,b=map(int,input().split(" x "))
c=0
for i in range(a):
    for k in range(b):
        if (i+k)%2==0 :
            c=c+1
print(a*b-c)


#by kshitiz
