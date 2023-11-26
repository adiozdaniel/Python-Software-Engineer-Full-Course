'''
A tuple is a sequence of immutable Python objects.
Meaning, tuples cannot be changed like lists. They can be overwritten
Tuples use parentheses while lists use square brackets
'''

tup = ('Mac', 'Linux', 'Windows', 'Android', 'Solaris', 'iOS')
# tup = (300, 500, 600, 700)

print("\n==========================================================\n")
print('Printing a Tuple!\n')
# print(tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])

# Using For Loop
for tup in tup: print(tup)

# Overwriting a tuple
tup = ('Windows', 'Android', 'iOS')
print(tup) # It overwrites the original tuple

# End of the program
print("\n==========================================================\n")
