name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks (0-100): "))

percentage = marks

print("\n--- Student Result ---")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Percentage:", percentage, "%")

if marks >= 35:
    print("Result: PASS")

    if marks >= 80:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: D")

else:
    print("Result: FAIL")
    print("Grade: F")
