import calculations.add,calculations.multi,factorial
import sys
def calc(*args):
    input_values = list(args)
    if str(input_values[1]) == '+':
        return calculations.add.adding(input_values[0])
        # print(tuple(input_values[0]))
print(calc([1,2,3,4,5,6],'+'))