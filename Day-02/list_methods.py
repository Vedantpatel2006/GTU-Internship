list1 = [2, 3, 4, 5, 6, 66, 77, 88, 99]

print(list1)

list1.append(111)
print("append:", list1)

list1.extend([22, 33])
print("extend:", list1)

list1.insert(2, 44)
print("insert:", list1)

list1.remove(66)
print("remove:", list1)

list1.pop()
print("pop:", list1)

print("index:", list1.index(77))

print("count:", list1.count(88))

list1.sort()
print("sort:", list1)

list1.reverse()
print("reverse:", list1)
