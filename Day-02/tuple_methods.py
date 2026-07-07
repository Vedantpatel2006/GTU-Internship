t = (10,20,30,20,40)

print(type(t))
print(t)

print("count:", t.count(20))
print("index:", t.index(30))
print("length:", len(t))
print("slice:", t[1:4])

t2 = t + (50,)
print(t2)
