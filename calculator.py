from tkinter import *
import math

# This function appends the clicked button's value to the expression
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# Clears the display
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

# Evaluates the expression
def btnEqualsInput():
    global operator
    try:
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""
    except:
        text_Input.set("Error")
        operator = ""

# Calculates square root
def btnSqrt():
    global operator
    try:
        result = str(math.sqrt(eval(operator)))
        text_Input.set(result)
        operator = ""
    except:
        text_Input.set("Error")
        operator = ""

# Adds exponentiation to the expression
def btnPower():
    global operator
    operator += "**"
    text_Input.set(operator)

# Main calculator window
cal = Tk()
cal.title("Simple Calculator")

operator = ""
text_Input = StringVar()

# Display
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="#f0f0f0", justify='right')
txtDisplay.grid(columnspan=4)

# Button styling
button_bg = "#a2d5f2"  # Light blue for numbers
op_bg = "#77dd77"  # Light green for operations
clear_bg = "#ff6961"  # Light red for clear button
equals_bg = "#fdfd96"  # Yellow for equals
button_font = ('arial', 20, 'bold')

# Buttons

# First Row
btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="7", bg=button_bg, command=lambda: btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="8", bg=button_bg, command=lambda: btnClick(8))
btn8.grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="9", bg=button_bg, command=lambda: btnClick(9))
btn9.grid(row=1, column=2)

btnAdd = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="+", bg=op_bg, command=lambda: btnClick("+"))
btnAdd.grid(row=1, column=3)

# Second Row
btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="4", bg=button_bg, command=lambda: btnClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="5", bg=button_bg, command=lambda: btnClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="6", bg=button_bg, command=lambda: btnClick(6))
btn6.grid(row=2, column=2)

btnSub = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="-", bg=op_bg, command=lambda: btnClick("-"))
btnSub.grid(row=2, column=3)

# Third Row
btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="1", bg=button_bg, command=lambda: btnClick(1))
btn1.grid(row=3, column=0)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="2", bg=button_bg, command=lambda: btnClick(2))
btn2.grid(row=3, column=1)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="3", bg=button_bg, command=lambda: btnClick(3))
btn3.grid(row=3, column=2)

btnMul = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="*", bg=op_bg, command=lambda: btnClick("*"))
btnMul.grid(row=3, column=3)

# Fourth Row
btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="0", bg=button_bg, command=lambda: btnClick(0))
btn0.grid(row=4, column=0)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="C", bg=clear_bg, command=btnClearDisplay)
btnClear.grid(row=4, column=1)

btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="=", bg=equals_bg, command=btnEqualsInput)
btnEquals.grid(row=4, column=2)

btnDiv = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="/", bg=op_bg, command=lambda: btnClick("/"))
btnDiv.grid(row=4, column=3)

# Fifth Row
btnSqrt = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="√", bg=button_bg, command=btnSqrt)
btnSqrt.grid(row=5, column=0)

btnPower = Button(cal, padx=16, pady=16, bd=8, fg="black", font=button_font, text="^", bg=button_bg, command=btnPower)
btnPower.grid(row=5, column=1)

# Add a blank button for spacing to center the last row
blankButton = Button(cal, padx=16, pady=16, bd=8, state=DISABLED, bg="#f0f0f0")  # Just for spacing
blankButton.grid(row=5, column=2)

blankButton2 = Button(cal, padx=16, pady=16, bd=8, state=DISABLED, bg="#f0f0f0")  # Second spacing button
blankButton2.grid(row=5, column=3)

# Start the application
cal.mainloop()
