from collections import defaultdict

indices = defaultdict(list)
#n, m = [int(x) for x in input().split()]

f1 = open('groupA.txt', 'r')
f2 = open('groupB.txt', 'r')

groupA = f1.readlines()
groupB = f2.readlines()
for i in range(len(groupA)):
    indices[i].append(i+1)
f1.close()
f2.close()

#for i in range(n):
#    groupA.append(input())
#for i in range(m):
#    groupB.append(input())
    

f3 = open('output.txt','w')

#for i in list(indices.values()):
#    a = [str(x) for x in i]
#    f3.write(" ".join(a)+'\n\n')
#f3.close()

for word in groupB:
    if word in indices:
        f3.write(indices[word])
    else:
        f3.write('-1\n')
f3.close()
