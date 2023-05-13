num_list = { i for i in range(26)}

sqr_list = {i ** 2 for i in range(1,25)}

even_list = { i for i in sqr_list if i%2 ==0}

print(num_list)
print(sqr_list)
print(even_list)

# Dict Comprehesions
import string
char_list = ','.join(string.ascii_lowercase).split(',')

sample_dict = dict(zip(num_list,char_list))

upd_dict = {i**2:j*2 for i,j in sample_dict.items()}

print(upd_dict)