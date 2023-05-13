from time import time
def fib(number):

    start = time()
    var1 = 0
    var2 = 1
    for i in range(number):
        yield var1
        temp = var1
        var1 = var2
        var2 = temp + var2
    end = time()

    total = end-start
    print(total)
    # return var1

for i in fib(50000):
    print(i)