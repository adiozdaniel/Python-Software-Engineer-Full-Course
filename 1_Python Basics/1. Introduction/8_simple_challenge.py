# Simple program to calculate age
print("Answer the questions to know how long you've taken on Earth...")
name = input("Name: ")
print("What is your age", (name), "?")
age = int (input ("age: "))

# int means integer such as 1,2,3 or -1, -2, -3
days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, 'has lived for ', days, " days ", minutes, " minutes and ", seconds, " seconds!")
print("Thank you for using this program")