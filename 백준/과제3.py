import itertools
R = [[0]*5 for i in range(5)]
R[0] = [0, 4, 8, 9, 12]
R[1] = [4, 0, 6, 8, 9]
R[2] = [8, 6, 0, 10, 11]
R[3] = [9, 8, 10, 0, 7]
R[4] = [12, 9, 11, 7, 0]
pool = ['1','2','3','4']
orderlist = list(map(''.join, itertools.permutations(pool)))
print(len(orderlist))
result = []
for order in orderlist:
    final = 0
    for i in range(4):
        if int(i) == 0:
            final += R[0][int(order[0])]
        elif int(i) == 3:
            final += R[int(order[3])][0]
        else:
            final += R[int(order[i])][int(order[i+1])]
    result.append(final)
print(result)
print(min(result))
