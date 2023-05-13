from functools import reduce
def reducefun(num,item):
    return num + item

a = reduce(reducefun,[i for i in range(10)],2)
print(a)