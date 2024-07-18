# Create dictionary

Dict = dict([(1, "Rohan"), (2, "Sumit"), (3, "Aditya"), (5, "Akash"), (4, "Kartik")])
print("Dictionary with each item as a pair:", Dict)  # Printing dictionary

# Adding element in dictionary
Dict[6] = 'Happy'
print("\n Dictionary with new item added:", Dict)

# Updating values in dictionary
Dict[3] = 'Aditya'
print("\n Dictionary with updated values:", Dict)

print("\n Accessing one value in Dictionary:", Dict[1])

# Deleting value from dictionary
del Dict[6]
print("\n Delete a value from a Dictionary:", Dict)

# Creating a nested dictionary
Dict1: dict[int, str | dict[str, str | int]] = {1: 'Rohan', 2: 'Sumit',
                                                3: {'Age': 21, 'Branch': 'IT', 'Year': 'Fourth Year'}}
print("\n Nested loop Dictionary:", Dict1)

print("\n Accessing an element of a Nested Dictionary:", Dict1[2])
