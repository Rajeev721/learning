input_list = ['a', 'b', 'c', 'd', 'c', 'd', 'e', 'f', 'r', 'g', 't', 'h']
new_list = []
for i in input_list:
    if input_list.count(i) > 1:
        if i not in new_list:
            new_list.append(i)

a = list(set([ i for i in input_list if input_list.count(i)> 1]))

print(new_list)

print(a)
