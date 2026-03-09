# def doubled(x):
#     return x * 2
# result = doubled(44)
# print(result)


square = lambda num : num * num

value = square(10)
print(value)

sum = lambda a, b, c : a + b + c

sum_result = sum(10, 20, 30)
print(sum_result)

arr = [1,2, 3, 4, 5]
print(arr)

sqr = map(square, arr)

cpy = sqr

# print(*cpy)
print(list(sqr))


sum_num = map(lambda a : a + a, arr)
print(list(sum_num))

cube = map(lambda x: x**3, arr)
print(*cube)

