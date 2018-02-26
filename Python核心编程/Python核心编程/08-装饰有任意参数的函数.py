import time


def gettime(func):
    def inner(*args, **kwargs):  # 将收到数据的打包
        begin = time.time()
        # 将被装饰的函数返回值暂存
        ret = func(*args, **kwargs)  # 将收到的参数拆包为收到的样子
        end = time.time()
        print("函数花费%f" % (end-begin))
        return ret
    return inner

@gettime
def f1():
    print("in f1")
    for i in range(1):
        time.sleep(1)

@gettime
def f2(number2):  # f2 = gettime(f2)
    print("number2 = %d" % number2)
    time.sleep(0.2)
    print("in f2")
    return 100

f1()
print(f2(100))