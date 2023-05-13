def mapfunc(num):
    return num * num +1

a = list(map(mapfunc, [i for i in range(10)]))

print(a)

b = list(map( lambda x: x*x+1,  [i for i in range(10)]))
print(b)
if a ==b:
    print("both lists are same")
else:
    print("please re verify the code")