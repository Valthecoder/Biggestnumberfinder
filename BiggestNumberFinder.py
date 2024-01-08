# Ask user for three inputs. Check if vowel or consonant
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))

if num2 < num1 and num3 < num1:
    print("The Biggest Number is: Num 1")
elif num1 < num2 and num3 < num2:
    print("The Biggest Number is: Num 2")
elif num1 == num2 == num3:
    print("All Numbers are Equal")
else:
    print("The Biggest Number is: Num 3")

# Design for wow factor
# Display a new window using message box
# Change some variables and functions since new window will be used
# Input Labels
# Create Button for trigger