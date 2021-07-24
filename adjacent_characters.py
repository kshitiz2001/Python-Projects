s=input()
if len(s) % 2 != 0:
    print("Odd length.")
else:
    print(''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ]))

#by kshitiz
