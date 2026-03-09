def test(recieved):
    print("start")
    recieved()
    print("ended")

def perametered_fun():
    print("this is peremetered function")

test(perametered_fun)