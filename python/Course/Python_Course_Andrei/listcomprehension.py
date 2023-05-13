num_list = [ i for i in range(1,25)]

sqr_list = [i ** 2 for i in range(1,25)]

even_list = [ i for i in sqr_list if i%2 ==0]

print(num_list)
print(sqr_list)
print(even_list)