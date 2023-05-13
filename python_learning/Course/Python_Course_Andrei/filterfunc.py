def filterfunc():
    a= list(filter(lambda x: x%2 ==0,  [i for i in range(10)]))
    print(a)

filterfunc()