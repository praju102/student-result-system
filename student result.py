name=input("enter your name:")
age=int(input("enter your age:"))
marks=int(input("enter your marks:"))
percentage=marks

print("\n...Student Result...")
print("Name:",name)
print("age:",age)
print("Marks:",marks)
if marks>=35:
    print("result pass")
else:
    print("result FAil")
print("percentage:",percentage,"%")
if marks>=80:
    print("garde A")
elif marks>=60:
    print("grade B")
elif marks>=35:
    print("grade C")
else:
    print("Fail")