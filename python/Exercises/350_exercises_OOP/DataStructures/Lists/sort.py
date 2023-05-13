text = 'Python programming'
text = list(set(text.lower().replace(" ", '')))
text.sort()
print(text)
# //////////////////////////////////////////
text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters)
# /////////////////////////////////////////////////////////////////////////////////////////////////
