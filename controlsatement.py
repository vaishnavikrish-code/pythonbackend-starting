# Get inputs
name = input("Enter student's name: ")
grade = int(input("Enter grade level (1-12): "))
base_fee = float(input("Enter base tuition fee: "))
discount_percent = 0

# Input for academic topper status
topper_input = input("Is the student an academic topper? (yes/no): ").strip().lower()

# Validate grade
if grade < 1 or grade > 12:
    print(" Invalid grade! Grade level must be between 1 and 12.")
else:
    # Conditional discount logic
    if 9 <= grade <= 12:
        if topper_input == "yes":
            discount_percent = 20
        else:
            discount_percent = 10
    elif 6 <= grade <= 8:
        discount_percent = 5
    else:
        discount_percent = 0

    # Calculate discount and final fee
    discount_amount = (discount_percent / 100) * base_fee
    final_fee = base_fee - discount_amount

    # Display result
    print("\n------ Tuition Fee Summary ------")
    print(f"Student Name     : {name}")
    print(f"Grade Level      : {grade}")
    print(f"Academic Topper  : {topper_input.capitalize()}")
    print(f"Base Tuition Fee : ₹{base_fee:,.2f}")
    print(f"Discount Applied : {discount_percent}%")
    print(f"Discount Amount  : ₹{discount_amount:,.2f}")
    print(f"Final Tuition Fee: ₹{final_fee:,.2f}")
