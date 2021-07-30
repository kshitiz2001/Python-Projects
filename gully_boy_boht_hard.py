st = input()
st = st.replace(' ','')

node = int(input())-1
rp = int(input())


result = (st[node:]+st[:node])*rp

for i in result:
    if i !=' ':
        print(i,end =' ')

#by kshitiz
