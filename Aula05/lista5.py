n1 = [1,43,2137,97,2,23,9]
n2 = [23,73,8,89,2,43,9,2347,86,234]
n3 = []
n3 = []


for i  in n1:
    for j in n2 :
        if i == j:
            n3.append(i)
print(n3)

for p  in n1:
    for s in n2 :
        if p % s == 0:
            n3.append(p)
print(n3)