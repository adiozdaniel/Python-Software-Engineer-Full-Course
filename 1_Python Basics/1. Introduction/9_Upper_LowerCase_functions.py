def lowercase(s):
    result = ""
    for c in s:
        if 65 <= ord(c) <= 90:  # ASCII range for uppercase letters
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

def titlecase(s):
    result = ""
    capitalize_next = True
    for c in s:
        if 65 <= ord(c) <= 90:  # ASCII range for uppercase letters
            result += chr(ord(c) + 32)
            capitalize_next = False
        elif 97 <= ord(c) <= 122:  # ASCII range for lowercase letters
            result += c if capitalize_next else chr(ord(c) - 32)
            capitalize_next = False
        else:
            result += c
            capitalize_next = True
    return result

def capitalized(s):
    result = ""
    capitalize_next = True
    for c in s:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:  # ASCII range for letters
            if capitalize_next:
                result += chr(ord(c) - 32)
                capitalize_next = False
            else:
                result += c
        else:
            result += c
            capitalize_next = True
    return result

def uppercase(s):
    result = ""
    for c in s:
        if 97 <= ord(c) <= 122:  # ASCII range for lowercase letters
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

print("\n====================================================\n")
print('\t CHANGING CASE!\n')

firstname = input("Enter your first name: ")
lastname = input('Enter your last name: ')

print('\n CHANGING CASE USING PYTHON INBUILT FUNCTIONS!\n')

print('To lowercase:\t{} {}'.format(firstname.lower(), lastname.lower()))
print('To uppercase:\t{} {}'.format(firstname.upper(), lastname.upper()))
print('To titlecase:\t{} {}'.format(firstname.title(), lastname.title()))
print('To capitalized:\t{} {}'.format(firstname.capitalize(), lastname.capitalize()))
print("\n====================================================\n")

print('\n CHANGING CASE USING ASCII VALUES!\n')

print('To lowercase:\t{} {}'.format(lowercase(firstname), lowercase(lastname)))
print('To uppercase:\t{} {}'.format(uppercase(firstname), uppercase(lastname)))
print('To titlecase:\t{} {}'.format(titlecase(firstname), titlecase(lastname)))
print('To capitalized:\t{} {}'.format(capitalized(firstname), capitalized(lastname)))

# End of the Changing Case
print("\n====================================================")
print("====================================================\n")
