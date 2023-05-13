a = [1,2,3,4,5,6,7]
print(a)

a.append([1,2,7]) # append - -add the list at the end as a list
print("The appended list is:{a}")

a.extend([9,10,11]) #Extend -- add the list at the end as items
print("The extended list is:{a}")

# a.clear() # clear -- clear the list

b = a.copy() # copy -- copy the items to a different object
print(f"The original list is:{a}")
print(f"The new list is:{b}")

a = [1,2,2,3,4,2,2,2,4,5,6,7] #count -- count the number of instances of passed item
print("The count of 2 in list a is:",a.count(2))

print('The indx is',a.index(2,3)) #index -- returns the item index

b.insert(7,98) # insert -- insert(location,value)
print(b)

b.pop() # pop -- removes item at given index, if none is passes remove item at the end of the list
print("pop function with no parameters")
print(b)
print("pop function with parameters")
b.pop(1)
print(b)

b = [1,2,2,2,2,2,2,23,5,6] #remove -- removes the first element in the list if the value is there, if the value is not there then it will thorow ValueError
b.remove(2)
print(b)

b.reverse() # reverse -- reverse the order of items in list
print(b)

b.sort() #sort
print(b)

print("first 2 elements are ", b[:2]) #Slicing