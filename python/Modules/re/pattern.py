import re
txt = "The raining in Spain"
pattern = re.compile("The raining in")

print("pattern searching",pattern.search(txt))
print("pattern split",pattern.split(txt))
print(re.sub("a","1",txt))
print("pattern findall",pattern.findall(txt))
print("pattern match",pattern.match(txt))
print("pattern match",pattern.finditer(txt))
print("pattern match",pattern.fullmatch(txt))