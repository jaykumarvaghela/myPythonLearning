heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Length of list

count = 0
for i in heros: count += 1
print(count)

# Add 'black panther' at the end of this list

heros.append('black panther')
print(heros)

"""
You realize that you need to add 'black panther' after 'hulk',
so remove it from the list first and then add it after 'hulk'
"""
heros.pop()
indx = heros.index('hulk')
heros.insert(indx + 1, 'black panther')
print(heros)

"""
Now you don't like thor and hulk because they get angry easily :)
So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
Do that with one line of code.
"""

heros[1:3] = ['doctor strange']
print(heros)

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print(dir(heros))
heros.sort()
print(heros)
