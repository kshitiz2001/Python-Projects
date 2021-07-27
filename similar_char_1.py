n = int(input())
s = input()
for i in range(int(input())):
    p = int(input())
    c = s[p-1]
    print(s[:p-1].count(c))

# by kshitiz
