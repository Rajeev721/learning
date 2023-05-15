import re

txt = "The raining in Spain"

element = re.search("rain", txt)

print(element.span())
print(element.start())
print(element.end())
print(element.group())