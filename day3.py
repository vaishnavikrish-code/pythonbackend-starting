
#list comprehension
num=[1,2,3,4,5]
print(f"{num}")
dod_num=[i*2 for i in num ]
print(f"{dod_num}")

num=[1,2,3,4,5,6,7,8,9,10]
even_num=[i for i in num if i%2==0]
print(f"{even_num}")

words=["apple","banana","cherry","date"]
upper_words=[word.upper() for word in words]
print(f"{upper_words}")

print(">> EXAMPLE 5: Numbers squared, only if > 2")
numbers = [1, 2, 3, 4, 5]
result = [num**2 for num in numbers if num > 2]
print(f"Original: {numbers}")
print(f"Squared (>2): {result}\n")

numbers = [1, 2]
letters = ['a', 'b']
combinations = [(num, letter) for num in numbers for letter in letters]
print(f"Numbers: {numbers}, Letters: {letters}")
print(f"Combinations: {combinations}\n")

#dictionary operations
num=[1,2,2,3,3,3,4,4,4,4]
count_dict={}
for i in num:
    count_dict[i]=count_dict.get(i,0)+1
print(f"Count dictionary: {count_dict}")

dic1={"a":1,"b":2}
dic2={"b":3,"c":4}
mrg={**dic1,**dic2}
print(f"Merged dictionary: {mrg}")

grads={"Alice":90,"Bob":85,"Charlie":92,"David":67}
high_grads={name: grade for name, grade in grads.items() if grade >= 70}
print(f"High grades: {high_grads}")

#set operations
num={1,2,2,3,3,4,5}
unique=set(num)
print("{num}")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set1 - set2
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Difference: {difference}\n")

#tuple un packing and multiple assigments


coor=(10,20)
X,Y=coor
print(f"{coor}")
print(f"X={X},Y={Y}")


val=[1,2,3]
a,b,c=val
print(f"{val}")
print(f"a={a},b={b},c={c}")

x,y=5,10
x,y=y,x
print(f"x={x},y={y}")


def get_name_age():
    return("alice",24)
name, age=get_name_age()
print(f"name={name},age={age}")

numbers = [1, 2, 3, 4, 5]
*first, middle, last = numbers
print(f"Numbers: {numbers}")
print(f"first = {first}, middle = {middle}, last = {last}")

#error handling:
try:
   num = int("abc")
   print(f"Success: {num}")
except ValueError:
   print("Error: Cannot convert to integer")

def process_input(val):

   try:
      num=int(val)
      result=100/num
      print(f"{result}")
      return result
   except ValueError:
      print("input must be number")
   except ZeroDivisionError:
      print("cannot divide")

process_input("25")
process_input("abc")
process_input("0")
print()


#defult arguments :
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Uses default greeting
greet("Bob", "Hi")                # Overrides default
greet("Charlie", greeting="Hey")  # Named parameter
print()

def power(base, exponent=2):
    return base ** exponent

print(f"2^2 = {power(2)}")         # Uses default exponent
print(f"2^3 = {power(2, 3)}")      # Override exponent
print(f"5^2 = {power(5)}")
print()


def search(items, target, case_sensitive=True):
    if not case_sensitive:
        target = target.lower()
        items = [item.lower() for item in items]
    return target in items

words = ["Hello", "World", "Python"]
print(f"'hello' in {words} (case sensitive): {search(words, 'hello')}")
print(f"'hello' in {words} (case insensitive): {search(words, 'hello', False)}")
print()