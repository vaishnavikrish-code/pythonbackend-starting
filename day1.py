
name = "Alice"              # String
age = 25                    # Integer
height = 5.7                # Float
is_student = False          # Boolean
empty_value = None 


print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Student: {is_student}, Type: {type(is_student)}")
print(f"None value: {empty_value}, Type: {type(empty_value)}")

#multiple assignment
x, y, z = 10, 20, 30
print(f"x: {x}, y: {y}, z={z}")
#swap 
a, b = 5, 10
print(f"before swap: a={a},b={b}")
a,b=b,a
print(f"after swap: a={a},b={b}")

#data types:

num1 = 42
num2 = -15
num3 = 0
print(f"integers: {num1}, {num2}, {num3}")
print(f"operations on integers: {num1 + num2}, {num1 - num2}, {num1 * num2}, {num1 / num2},{num1 // num2}, {num1 % num2}, {num1 ** 2}")

print("\n>> FLOATS")
pi = 3.14159
temp = -5.5
print(f"Floats: {pi}, {temp}")
print(f"Float operation: {pi * 2}")

print("\n>> STRINGS")
text1 = "Hello, World!"
text2 = 'Single quotes work too'
text3 = """Multi-line
string works
like this"""

print(f"String 1: {text1}")
print(f"String 2: {text2}")
print(f"String 3:\n{text3}")

#indexing
word = "python"
print(f"Word: {word}")
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"word[5]: {word[5]}")
print(f"word[-2]: {word[-2]}")

#slicing
print(f"word[0:4]: {word[0:4]}") #0,1,2,3
print(f"word[1:4]: {word[1:4]}")#1,2,3
print(f"word[:4]: {word[:4]}")#start to index 3
print(f"word[2:]: {word[2:]}")#start 3 to end
print(f"word[::-1]: {word[::-1]}")  # Reverse the string
print(f"word[::2]: {word[::2]}")  # Every second character

print("\n>> BOOLEANS")
flag1 = True
flag2 = False
print(f"Booleans: {flag1}, {flag2}")
print(f"not True = {not flag1}")
print(f"True and False = {flag1 and flag2}")
print(f"True or False = {flag1 or flag2}")


print("\n>> LOGICAL OPERATORS")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")


# MEMBERSHIP OPERATORS
print("\n>> MEMBERSHIP OPERATORS")
letters = ['a', 'b', 'c']
print(f"letters = {letters}")
print(f"'a' in letters: {'a' in letters}")
print(f"'z' in letters: {'z' in letters}")
print(f"'z' not in letters: {'z' not in letters}")

#LISTS, TUPLES, SETS, DICTIONARIES:

#list
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]


print(f"numbers = {numbers}")
print(f"numbers[0] = {numbers[0]} (first element)")
print(f"numbers[-1] = {numbers[-1]} (last element)")

tuple
coords = (10, 20)
rgb = (255, 128, 0)

print(f"coords = {coords}")
print(f"coords[0] = {coords[0]}")

#SET - Unordered, unique elements only
print("\n>> SETS (Unique, Unordered)")
colors = {"red", "blue", "green"}
print(f"colors = {colors}")

colors.add("yellow")
print(f"After add('yellow'): {colors}")


# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"\nset1 = {set1}, set2 = {set2}")
print(f"set1 & set2 (intersection) = {set1 & set2}")
print(f"set1 | set2 (union) = {set1 | set2}")
print(f"set1 - set2 (difference) = {set1 - set2}")


# DICTIONARY - Key-Value pairs
print("\n>> DICTIONARIES (Key-Value)")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": True
}

print(f"person = {person}")
print(f"person['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('job', 'Unknown') = {person.get('job', 'Unknown')} (default value)")

person['age'] = 26
print(f"After setting age to 26: {person}")

person['job'] = 'Engineer'
print(f"After adding job: {person}")

del person['job']
print(f"After deleting job: {person}")

print(f"\nperson.keys() = {list(person.keys())}")
print(f"person.values() = {list(person.values())}")
print(f"person.items() = {list(person.items())}")

#string methods
text = "Hello, World!"

print(f"\nOriginal string: '{text}'")
print(f"text.lower() = '{text.lower()}'")
print(f"text.upper() = '{text.upper()}'")
print(f"text.capitalize() = '{text.capitalize()}'")
print(f"text.strip() = '{text.strip()}' (removes leading/trailing whitespace)")
print(f"text.replace('World', 'Python') = '{text.replace('World', 'Python')}'")
print(f"text.split(',') = {text.split(',')}")
print(f"'-'.join(['Hello', 'World']) = {'-'.join(['Hello', 'World'])}")
print(f"text.find('World') = {text.find('World')} (index of substring, -1 if not found)")
print(f"text.startswith('Hello') = {text.startswith('Hello')}")
print(f"text.endswith('!') = {text.endswith('!')}")
print(f"text.isdigit() = {text.isdigit()}")
print(f"'12345'.isdigit() = {'12345'.isdigit()}")

# TYPE CONVERSION

print(f"int('42') = {int('42')}")
print(f"int(3.7) = {int(3.7)} (truncates, doesn't round)")
print(f"int(True) = {int(True)}")

# Convert to float
print(f"float('3.14') = {float('3.14')}")
print(f"float(42) = {float(42)}")

# Convert to string
print(f"str(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")

# Convert to bool
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool('') = {bool('')} (empty string is False)")
print(f"bool([]) = {bool([])} (empty list is False)")


#questions:

#temperature conversion: Celsius to Fahrenheit

#c=(f-32)*5/9
#32f

f= 32
c = (f - 32) * 5 / 9
print(f"{c} degrees celsius")

#2sol a.upper case,b.reverse string,c.index of 'o'

word = "python"
print(f"word.upper() = {word.upper()}")
print(f"word[::-1] = {word[::-1]}")
print(f"word.index('o') = {word.index('o')}")

