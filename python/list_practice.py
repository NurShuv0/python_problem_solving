nur_list = [5, 1, 2, 3, 4, 5, 6, 777, 8, 9, 10]
print(nur_list[2], nur_list[-6])

print(nur_list[2:8])

print(nur_list[2:8:2])

print(nur_list[8:2:-1])
print(nur_list)

#reverse

print(nur_list[::-1])

nur_list.append(100)
print(nur_list)

nur_list.insert(5,5)
print(nur_list)

nur_list.remove(5)
print(nur_list)

if 55 in nur_list:
    nur_list.remove(55)

last = nur_list.pop()
print(last)
print(nur_list)
index = nur_list.index(10)
print(index)

cnt = nur_list.count(5)
print(cnt)

nur_list.sort()
print(nur_list)
