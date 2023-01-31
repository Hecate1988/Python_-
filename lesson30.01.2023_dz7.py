lst = [0,3,6,3,6,2,6,8,6,0,3,0,9,7,0,0,4]
#lst = [0]
#lst = [1,0,1,0,4,3,0]
#lst = []
for i in range(len(lst)-1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))
print(lst)



