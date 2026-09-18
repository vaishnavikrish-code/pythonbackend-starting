##control flow statements
#while loop
#countdown  5 to 1
count = 5
while count >0:
    print(count)
    count -= 1

#Repeat until user says stop (simulated)
user_input = ""
while user_input.lower() != "stop":
    user_input = input("Type 'stop' to end the loop: ")
    print(f"You entered: {user_input}")


# different 
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    attempts += 1
print("Maximum attempts reached! \n")

#SUM OF NUM UNTILL REACH TARGET
total = 0
num = 1
target = 10
while total < target:
    total += num
    print(f"added{num}, total = {total}")
    num +=1
print(f"reached target {target}")

#loops condition

count = 5
while count > 0:
    print(count)
    count -= 1 


#break and continue
# find item and stop 
num = [1,2,3,4,5,6,7,8,9,10]
target = 8
for i in num:
    if i ==  target:
        print(f"Found target {target}!")
        break
    print(f"Checking {i}")
print()

#password attempts


correct_password="python"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_password = input("Enter password: ")
    if user_password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Incorrect password. Attempts left: {max_attempts - attempts}")

#skip add nums
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

#nested loop

for i in range(1, 4):
    for j in range(1,4):
        print(f" {i} *  {j} = {i * j}", end=" ")
    print()   



#2D grid


for i in range(1,5):
    for j in range(1,5):
        print(f"  ■", end=" ")
    print()
print()

#loop brak
found = False
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            print(f"  Found target at position ({i}, {j})")
            found = True
            break
    if found:
        break
print()
