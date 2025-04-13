# String in Python
message = "  Hello, Python World!  "

# Display the original string
print("Original string:", repr(message))

# String Methods

# 1. strip() - removes leading and trailing spaces
cleaned = message.strip()
print("After strip():", repr(cleaned))

# 2. lower() - converts to lowercase
lowercase = cleaned.lower()
print("After lower():", lowercase)

# 3. upper() - converts to uppercase
uppercase = cleaned.upper()
print("After upper():", uppercase)

# 4. replace() - replaces substring with another
replaced = cleaned.replace("Python", "Hemant")
print("After replace():", replaced)

# 5. split() - splits the string into a list
words = cleaned.split()
print("After split():", words)

# 6. find() - finds the index of a substring
index = cleaned.find("Python")
print("Index of 'Python':", index)

# 7. isalpha() - checks if all characters are alphabets
only_alpha = cleaned.isalpha()
print("Is all alphabetic (isalpha()):", only_alpha)

# 8. len() - built-in function to get string length
length = len(cleaned)
print("Length of cleaned string:", length)

# 9. join() - joins a list of strings into a single string
joined = ", ".join(words)
print("After join():", joined)


# String Formatting

# 1. f-string (Python 3.6+)
name = "Hemant"
age = 20


# 2. format() method (Python 2.6+)
formatted = "Name: {}, Age: {}".format(name, age)
print("After format():", formatted)

# 3. % operator (Python 2.0+)
formatted = "Name: %s, Age: %d" % (name, age)
print("After % operator:", formatted)

# 4. Template strings (Python 2.4+)
from string import Template
template = Template("Name: $name, Age: $age")
formatted = template.substitute(name=name, age=age)
print("After template:", formatted) 
    


