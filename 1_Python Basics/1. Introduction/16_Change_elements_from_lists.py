pets = ["lion", "dragon", "horse", "bear"]

# change elements
pets[2] = "dog"
pets[3] = "eagle"
pets[0] = "cow"

print("This is the changed names of ", pets)
# delete elements
del pets[1]
del pets[2]
print("These are the remaining pets after deletion: ", pets)
