print("\n====================================================\n")
print('\t FIRST CHALLENGE: SIMPLE PROGRAM!\n')

name = input("What is your name?: ")
# more complex input with format specifier
age = input("{} what is your age?: ".format(name))
# picking .format arguments by their index or name
print("Wow, {1} is great {0}! \nThank you {noun} for using my simple program.".format(name, age, noun = name))

# End of the simple program
print("\n====================================================\n")
