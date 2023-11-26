# copy slicing helps in adding or editing your list without affecting the original list

OS = ['Mac', 'Linux', 'Windows', 'Android', 'Solaris', 'iOS']
cpy_OS = OS[:4]

print("\n==========================================================\n")
print('Printing a new sliced list!')
print(OS)
print('\nThe copy of OS: ')
# print(cpy_OS)

cpy_OS.append('Chrome')
cpy_OS.append('PyOS')
print(cpy_OS)

# End of the program
print("\n==========================================================\n")
