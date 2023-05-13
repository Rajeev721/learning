import re
with open(r'C:\Downloads\customer1638875051040.csv', mode= 'r', newline='\n') as f:
    for k,i in enumerate(f.readlines()):
        a = re.search("^[12]",i)
        # print(a)
        # 
        if a:
            print(a.start())
            print(a.group())
            print(a.groupdict())
            print(f"The line {k} starts with either 1 or 2")