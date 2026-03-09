nur_list = [5, 1, 2, 3, 4, 5, 6, 777, 8, 9, 10]

next_list = ["hey","you","gorib"]

# for item in nur_list:
#     print("Nur items : ", item)
#     for inner in next_list:
#         print(item, inner)

comprehension = [item for item in nur_list if item % 2 == 0 or item > 100]
print(comprehension)
