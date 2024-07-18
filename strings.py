# Different ways creating a string.

string = 'welcome'
print(string)

string = "Welcome"
print(string)

string1 = ''' to India '''
print(string1)

string2 = """Welcome to
           India full fill with different traditions and rituals. """  # triple quotes string can extend multiple lines
print(string2)
print()

# Concatenating two strings using + operator
str1 = string + string1
print("Concatenated two different strings:", str1)
print()

# Finding the length of the string.
print("length of the string:", len(str1))
print()

# Extract a string using Substring.

# Searching in strings using index()
str3 = 'Ashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:", str3.index(str1))
print("Position of h:", str3.index(str2))
print()

# Match a String Against a Regular Expression With matches().
import re

Substr = 'Virat'
str6 = 'Virat once said- Wake up to reality nothing goes as planned in this cursed world'
print(re.match(Substr, str6))
print()

# Comparing strings.
str8 = 'Itachi uchar'
str1 = 'Madara uchar'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()

# startsWith(), endsWith().
string = 'Minato Kamikaze'
print(string.startswith("Minato"))
print(string.endswith("kaze"))
print()

# Trimming strings with strip().
str7 = 'Welcome India hi'
print(str7.strip("hi"))
print()

# Replacing characters in strings with replace()
string = 'Hi Strangers'
print(string.replace("Hi", "Hello"))
print()

# Splitting strings with split()
str9 = 'hello-hi-bye_bye'
print(str9.split("-"))
print()

# Converting integer objects to Strings.
numb = 116
numb1 = str(numb)
print(numb1)
print(type(numb1))

print()
# Converting to uppercase and lowercase.
string = 'HELLO'
string1 = 'STRANGERS'
print(string.upper())
print(string1.lower())
