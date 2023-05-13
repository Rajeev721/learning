techs = ('python', 'java', 'sql', 'aws')

new_tech = list(techs)
new_tech.sort()
print(tuple(new_tech))

# ***********************************************************************************
techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)