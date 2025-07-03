L = [1, 1, 2, 2, 3]
O = dict()
for i in L:
    if i not in O:
        O[i] = 1
    else: O[i] += 1

print(O)

    


