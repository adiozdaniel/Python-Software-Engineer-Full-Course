# It is more easier to compare strings in Python than other languages like C

name = "Python"
language = "C++"
lesson = 'Python'

print("\n==========================================================\n")
print('\tMathematical Operations in decision making!\n')

print('\nEqual to (==):')
if name == language: print('The two strings are equal')
else: print('These seem to be different strings')

print('\nEqual to (==):')
if name == lesson: print('This is one and the same thing!')
else: print('These seem to be different strings')

print('\nNot Equal (!=):')
if name != lesson: print('Choose another lesson') # using Not Equal
else: print('You are in the right place!')

print('\nUsing \'and\' (&) to add more checks:') #if all condtions are tru
if name == lesson and name != language: print('You got it!') # replace the variables
else: print('Sooo complicated, does not meat the condition!')

print('\nUsing or (||):') # at least one condition is true
if name != lesson or name != language: print('This is very true for \'or\' checks') # using Not Equal
else: print('Ouch, one condition was not met!')

# End of the program
print("\n==========================================================\n")
#try numbers for variable values