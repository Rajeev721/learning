thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

new_dict = thisdict.copy() # copy()	Returns a copy of the dictionary
a = [1,2,3]
b = 'a'

c = dict.fromkeys(a,b) # fromkeys()	Returns a dictionary with the specified keys and value

print("the dictionary created using fromkeys is:",c)

print(thisdict.get("year")) # get()	Returns the value of the specified key
print(thisdict.get('name',"Rajeev")) # get() Returns the value of the specified key

print(thisdict.items()) # items()	Returns a list containing a tuple for each key value pair
print(thisdict.keys()) # keys()	Returns a list containing the dictionary's keys

thisdict.pop("year") # pop()	Removes the element with the specified key
print(thisdict)

thisdict.popitem() # popitem()	Removes the last inserted key-value pair
print(thisdict)

b = thisdict.setdefault("year",1345) # setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(b)

thisdict.update({"color":"red"}) # update()	Updates the dictionary with the specified key-value pairs
print(thisdict)

a = thisdict.values() # values()	Returns a list of all the values in the dictionary
print(a)
print(len(thisdict))

thisdict.clear() # clear()	Removes all the elements from the dictionary