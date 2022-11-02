import time

def timeme(func):

    def wrapper():
        start = time.time()
        func()
        ending = time.time()
        print("Total time %.2f seconds" % (ending-start))

    return wrapper