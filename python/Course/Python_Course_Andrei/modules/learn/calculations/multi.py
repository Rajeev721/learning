def multiply(*args):
    new_list = list(args[0])
    default_value = 1
    for i in new_list:
        default_value *= i
    return default_value