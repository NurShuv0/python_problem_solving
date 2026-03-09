import time
def timer(recieved_funtion):
    print("this is outer")
    def inner(*n):
        print("time started")
        start = time.time()
        recieved_funtion(*n)
        print("timer ended")
        end = time.time()
        print(end - start)
    return inner
@timer
def another(n):
    print("this is another function")
    print(f'the power of n is {n**n}')

# timer(another)()

another(100)