# Output in Burj Khalifa Pattern
def fib(a):
    if a <= 1:
        return a
    else:

        return fib(a-1) + fib(a-2)

num = int(input('enter the length of fibonacci series '))
for i in range(num):
    f = fib(i)
    print(f)

# Output In List Form
num = int(input('enter the length of fibonacci series '))

a = 0
b = 1
lst = []
lst.extend((a,b))
for i in range(num-2):
    temp = a + b
    lst.append(temp)
    a = b
    b = temp
print(lst)
