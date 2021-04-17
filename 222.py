a = [6, 3, -1, 4, 2, -1, 1]
b = []
count = -1
for i in a:
    count+=1
    if i == -1:
        b.append(count)
        a.remove(i)
for i in b:
    c.insert(-1,i)
print(sorted(c))
