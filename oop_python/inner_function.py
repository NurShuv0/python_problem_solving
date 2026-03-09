def outer_fun():
    print("this is outer function")
    def inner_fun():
        print("this is a inner function")
    # return inner_fun()
    return inner_fun

print(outer_fun()())