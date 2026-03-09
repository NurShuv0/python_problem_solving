nur_list = [1, 2, 3, 4, 5]
name_list = ["nur", "tarok", "tuhin", "shoshi", "taseen"]
pair = []
for i, j in zip(nur_list, name_list) : 
    print(i, j)
    pair.append([i,j])
# print(pair)

#by for loop in pair
for first, second in pair : 
    print(first, second)

