friends = [
    {"name":"nur", "rating": 100},
    {"name": "Tuhin", "rating":90},
    {"name": "prachurjo", "rating":80},
    {"name": "pushpo", "rating":20},
    {"name": "shoshi", "rating": 30},
    {"name": "taseen", "rating": 10}
]
print(friends)
temp = filter(lambda x: x["rating"] <= 50, friends)
# print(*temp)
print(list(temp))

div_3 = filter(lambda x: x["rating"] % 3 == 0, friends)
print(list(div_3))