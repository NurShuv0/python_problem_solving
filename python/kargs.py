# def name(first, last):
#     name = f'{first} {last}' 
#     return name
# name = name("nur", "shuvo")
# print(name)

# def name(first, last):
#     name = f'my full name is : {first} {last}' 
#     return name
# name = name(last = "shuvo", first = "nur")
# print(name)


# def famous_name(first, last, title, addition):
#     name = f'full name is : {title} {first} {last} {addition}'
#     return name

# print(famous_name(first = "nur", last = "shuvo", title = "md" , addition="mozumder"))


def kargs(first, second, **arguments):
    print(first, second)
    for key, value in arguments.items():
        print(key, value)

kargs(10,20,a = 30,b = 40, c = 50, d = 60, e = 70, f = 80, g = 90,h = 100)
     


