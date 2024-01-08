import tkinter as tk
import pygame


# Ask user for three inputs. Check if vowel or consonant
def find_and_print_biggest_number():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())

# Creating if functions
    if num2 < num1 and num3 < num1:
        result = "The Biggest Number is: Num 1"
    elif num1 < num2 and num3 < num2:
        result = "The Biggest Number is: Num 2"
    elif num1 == num2 == num3:
        result = "All Numbers are Equal"
    else:
        result = "The Biggest Number is: Num 3"

# Design for wow factor
    # Display a new window using messagebox
    print(result)
    show_result_message(result)


def show_result_message(result):
    # For the size of the messagebox
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    # Size of the result window
    result_window.geometry("600x150")

    # Create a Label to display the result in the custom window
    result_label = tk.Label(result_window, text=result, font=("Times", 30), fg="Red")
    result_label.pack(pady=20)


# Create a new window
root = tk.Tk()
root.title("Biggest Number Finder")

# Make size of the window bigger
root.geometry("500x350")

# Input labels
label1 = tk.Label(root, text="Enter the 1st Number(Num1):", font=("Times", 20), fg="Blue")
label1.pack()

entry1 = tk.Entry(root, font=("Times", 20))
entry1.pack()

label2 = tk.Label(root, text="Enter the 2nd Number(Num2):", font=("Times", 20), fg="Green")
label2.pack()

entry2 = tk.Entry(root, font=("Times", 20))
entry2.pack()

label3 = tk.Label(root, text="Enter the 3rd Number(Num3):", font=("Times", 20), fg="Dark Orange")
label3.pack()

entry3 = tk.Entry(root, font=("Times", 20))
entry3.pack()

# For some space between the input blank and the trigger button
tk.Label(root, text="").pack()

# Button for trigger with larger font size
calculate_button = tk.Button(root, text="Find Biggest Number", command=find_and_print_biggest_number,
                             font=("Times", 30), bg="Light Green")
calculate_button.pack()


root.mainloop()
