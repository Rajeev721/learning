from time import time
def squ(number):

    start = time()
    for i in range(number):
        yield i ** 2
    end = time()

    total = end-start
    print(total)

def squlist(num):
    start = time()
    for i in range(num):
        pass
    stop = time()
    tot = stop-start
    print(tot)

for i in squ(5000000):
    pass

squlist(5000000)