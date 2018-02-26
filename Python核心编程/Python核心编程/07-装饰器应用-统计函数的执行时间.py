import time

def gettime(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print("函数花费%f" % (end-begin))
    return inner

@gettime
def f1():
    print("in f1")
    for i in range(1):
        time.sleep(1)

@gettime
def f2():
    time.sleep(0.2)
    print("in f2")

f1()
f2()