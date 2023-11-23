# "In" Operator:
# Used to check if a specified object or variable exists
# within the list of variables

pet = "my dog"

if pet in ["lion", "cat", "my dog"]: #remove the 'my dog' and see results
    print("Your pet is IN the list")
else:
    print("Sorry, I couldn't find your pet")

if pet not in ["lion", "cat", "duck"]: #remove the 'my dog' and see results
    print("Kudos, your is NOT IN the slaughter list")
else:
    print("We are afraid your pet is on the slaughter list")