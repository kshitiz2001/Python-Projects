from itertools import combinations
input()
combos = list(combinations(input().split(), int(input())))
count = 0
for i in combos:
    if "a" in i:
        count+=1
print(round(count/len(combos),3))

# by kshitiz
