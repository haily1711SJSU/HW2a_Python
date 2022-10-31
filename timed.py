import time

def timeme(func):

    def wrapper():
        start = time.time()
        func()
        ending = time.time()
        print("Total time {0:.2f}".format(ending-start))

    return wrapper
