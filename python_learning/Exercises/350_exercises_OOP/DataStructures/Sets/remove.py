text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
text = text.lower().replace(' ', '').replace('.','')
letters = set(text)
letters = letters.difference(vowels)

print(f"Number of items: {len(letters)}")