n = int(input('enter the height of the pattern : '))
a = len(bin(n))-2

for b in range(n+1):
    b=bin(b)[2:]
    c=len(b)
    print(' '*(a-c)+b)
    
#     by kshitiz
