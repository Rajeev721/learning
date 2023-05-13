# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def parameters(cls,num1,num2):
        return cls('New_Cat', num1+num2)

    def oldest(self, *args):
        oldest_cat = 0
        for cat_age in args:
            for cat_age_next in args:
                if cat_age.age > cat_age_next.age:
                    oldest_cat = cat_age.age
        return oldest_cat



# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('abc', 10)
cat2 = Cat('BBC', 13)
cat3 = Cat('DDD', 15)

v = Cat.parameters(10, 20).name
w = Cat.parameters(10, 20).age

print(v)
print(w)
# 2 Create a function that finds the oldest cat
old_cat = Cat.oldest(cat1, cat2, cat3)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {old_cat} years old.")