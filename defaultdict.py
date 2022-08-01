from collections import defaultdict

indices = defaultdict(list)
#n, m = [int(x) for x in input().split()]

f1 = open('groupA.txt', 'r')
f2 = open('groupB.txt', 'r')
groupA = f1.readlines()
groupB = f2.readlines()
f1.close()
f2.close()

#for i in range(n):
#    groupA.append(input())
#for i in range(m):
#    groupB.append(input())
    
for word in groupB:
    if word not in groupA:
        indices[word].append(-1)
        continue
    for i in range(len(groupA)):
        if groupA[i] == word:
            indices[word].append(i+1)
f3 = open('output.txt','w')

for k,val in indices.items():
    a = [str(x) for x in val]
    f3.write(k+" ".join(a)+'\n\n')
f3.close()
