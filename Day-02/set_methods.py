set1 = {10,20,30}
set2 = {30,40,50}

print(set1)

set1.add(60)
print(set1)

set1.update(set2)
print(set1)

set1.remove(20)
print(set1)

print(set1.union(set2))

print(set1.intersection(set2))
