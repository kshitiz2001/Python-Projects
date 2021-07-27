n=int(input())
for i in range(0,n):
    a=set(input().upper())
    b=set(input())
    if b.issubset(a)== True:
        print("YES")
    else:
        print("NO")

# by kshitiz
