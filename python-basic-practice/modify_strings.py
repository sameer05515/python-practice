a = "Hello, World!"
print(a.upper())

print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
