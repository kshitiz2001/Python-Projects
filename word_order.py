n = int(input())
map = {}
count = 0
for i in range(n):
    word = input()
    if word not in map:
        map[word] = 1
        count += 1
    else:
        map[word] += 1
print(count)
for key, value in map.items():
    print(value, end = " ")
