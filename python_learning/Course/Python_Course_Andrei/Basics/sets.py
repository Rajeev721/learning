a = {1,2,3,4,5,6,7}
b = {5,6,7,8,9,10}

a.add(11) #Adds an element to the set
print("after adding an element to the set, the new set value is:",a)
c = a.copy() #Returns a copy of the set
print("the copied set is:",c)
a.clear() #Removes all the elements from the set
print("after clearing the set, it has",a)
a = c.copy()
diff_set = a.difference(b) #Returns a set containing the difference between two or more sets
print("the difference is:",diff_set)
a.difference_update(b)
print("the difference update method returns",a) #Removes the items in this set that are also included in another, specified set
a.discard(2) #Remove the specified item
print("the set has",a)

inersect = c.intersection(b) #Returns a set, that is the intersection of two or more sets
print(inersect)

a = c.copy()

print("updating set c usig insersection_update")

c.intersection_update(b)
print("the set has following items after intersection_update \n",c) # intersection_update() #Removes the items in this set that are not present in other, specified set(s)
print(a.isdisjoint(b)) #Returns whether two sets have a intersection or not
print("is C a subset of B:",c.issubset(b)) #Returns whether another set contains this set or not
print("is B a superset of C:", b.issuperset(c)) #Returns whether this set contains another set or not
c.pop()
print("after removing the element the set has:",c) #Removes an element from the set
c.remove(7)
print("after removing the element 7 the set has:",c)   #Removes the specified element

sym_diff  = a.symmetric_difference(b) #Returns a set with the symmetric differences of two sets
print(a,b,c)
print("sym_diff is:",sym_diff)

c = a.copy()
a.symmetric_difference_update(b)
print("symmetric_difference_update:",a) # symmetric_difference_update() #inserts the symmetric differences from this set and another
union_set = a.union(b) #Return a set containing the union of sets
print("sset after doing unionn on a,b is:",union_set)
a.update(b)
print(c)
print(a) #Update the set with another set, or any other iterable