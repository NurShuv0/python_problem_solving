arr = [1, 2, 3, 4]
arr2 = ["nur", "uddin", "prachurjo", "tuhin"]
dictionary = dict(zip(arr, arr2))

# for key, value in dictionary.items():
#     print(key, value)

# print(dictionary)
# for key, value in enumerate(dictionary):
#     print(key, value)
# dictionary.clear()

new = dictionary

print(dictionary)

print(new)

new[1] = "no one"

print(new[1])

popped_item = new.popitem()
print(popped_item)
