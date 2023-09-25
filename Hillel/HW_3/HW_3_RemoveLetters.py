string = input("Input string: ")
letter = input("Input letter what should be removed: ")
new_string = "".join([char for char in string if char != letter])
print(f"New string: {new_string}")