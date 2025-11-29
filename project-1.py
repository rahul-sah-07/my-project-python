# Day1 -check positive/negative and check odd/even

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# Check even or odd for non-zero values
if num != 0:
    if num % 2 == 0:
        print("It is an Even number")
    else:
        print("It is an Odd number")
