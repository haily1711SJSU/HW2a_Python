
import time

def timeme(func):

    def wrapper():
        start = time.time()
        func()
        ending = time.time()
        print("Total time {0:.2f}".format(ending-start))

    return wrapper

def two_sec():
    time.sleep(2)

two_passed = timeme(two_sec)
two_passed()
