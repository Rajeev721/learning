# def powerofnum(n,m):
#     power = 1
#     for i in range(m):
#         power *= n
#     print(power)
#
# powerofnum(2,6)



def powerofnum(a,b):
    if b == 0:
        return 1
    return (a*powerofnum(a,b-1))
    # print(val)

print(powerofnum(5,3))

