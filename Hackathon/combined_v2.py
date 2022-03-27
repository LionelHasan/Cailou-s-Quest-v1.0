import tkinter as tk
from tkinter import NW, font as tkfont
import os


list_of_answers = ['print(\'I love eating SPAGHETTI and MEATBALLS\')', 'integer_three = 3', 'string_three = \'3\'', 'print(\'The product of number one and number two is:\', number_one * number_two)', 'This person is unknown.', 'The number is one.']

def format_response(i):
    if i == 'Yes':
        return 'You are correct!'
    else:
        return 'You are incorrect'

class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = 'Verdana', size = 10, weight = 'normal')

        container = tk.Frame()
        container.grid(row=0,column=0,sticky='nesw')

        self.id = tk.StringVar()
        self.id.set('Caillou Quest')

        self.listing = {}


        for p in (page_1, page_2, page_3):
                page_name = p.__name__
                frame = p(parent = container, controller = self)
                frame.grid(row=0, column=0, sticky = 'nsew')
                self.listing[page_name] = frame
        self.up_frame('page_1')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()


class page_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        self.id = controller.id
        self.entry1 = tk.StringVar()

        def run():
            os.system('python T1MC1.py')

        label = tk.Label(self, text = controller.id.get(), font = controller.titlefont)
        label.pack()
        message = tk.Label(self, text= """
Topic 1 - Print Explanation
        
A print statement is a line of code used to display a message to the screen. Print statements can be set by the programmer, or adjusted by the user based on input given to the computer.
A print statement consists of a “print” command with a written message enclosed in a bracket and an apostrophe (or quotations).
Be aware that print statements and lines of code are case sensitive
A print statement is in the form of a string, where a string is a data-type used to display text
        
Example:
print(‘Hello’) → Output: Hello
print(“Happy BirtHday BOB!!!”) → Output: Happy BirtHday BOB!!!
Note: Be aware of capitals (it is case sensitive)\n\n""", font=controller.titlefont, justify='left')
        message.pack()

        answer = tk.Label(self, text='Use the proper syntax to display the message (please use apostrophes and not quotations): I love eating SPAGHETTI and MEATBALLS')
        answer.pack()

        answer_entry = tk.Entry(
            self, textvariable=self.entry1)
        answer_entry.pack()
        answer_entry.focus()

        bout = tk.Button(self, text = 'submit', command=lambda: answer_check(answer_entry.get()))
        bout.pack()
        
        btn = tk.Button(self, text='open game', command=run)
        btn.pack()

        def answer_check(entry):
            if entry == 'print(\'I love eating SPAGHETTI and MEATBALLS\')':
                response_label['text'] = format_response('Yes')
            else: 
                response_label['text'] = format_response('No')

        response_label = answer = tk.Label(self)
        response_label.pack()

        bou = tk.Button(self, text = '>>', command = lambda: controller.up_frame('page_2'))
        bou.pack()

class page_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        self.id = controller.id
        self.entry1 = tk.StringVar()

        def run():
            os.system('python T2MC1.py')


        label = tk.Label(self, text = controller.id.get(), font = controller.titlefont)
        label.pack()
        message = tk.Label(self, text= """
Topic 2 - Object Types (Variables, Integers, and Basic Mathematical Operations)

Integers are another data-type (like a string), used to represent numerical whole numbers.
Integers can be used in mathematical operations (using +, -, /, *).
The convention is to use one space between mathematical symbols (to make it easier to read).
Note: String versions of numbers cannot be used in mathematical operations. Integer values must be used.

Variables allow you to store values for later use, which can be helpful so you don’t have to repeat yourself a lot.
Variables are named references assigned to values using “=”. 
Variables can be assigned to strings or integers (or other data types).
Quotations and apostrophes are not required around variables (unlike strings).
If you are incorporating strings and variables in a single print statement, ensure commas are used to separate (with apostrophes and quotations enclosing ONLY the strings)

Example 1:
animal_type = ‘rabbits’
food_type = ‘carrots’
print(animal_type, ‘feed off of’, food_type)
Output: rabbits feed off of carrots

Example 2:
number_one = 1
number_two = 2
number_three = number_one + number_two
print(‘The sum of number one and number two is’, number_three)
Output: The sum of number one and number two is number three\n""", justify='left', font=controller.titlefont)
        message.pack()

        answer = tk.Label(self, text='Assign the variable "integer_three" to the integer version of "3".')
        answer.pack()

        answer_entry = tk.Entry(
            self, textvariable=self.entry1)
        answer_entry.pack()
        answer_entry.focus()

        bout = tk.Button(self, text = 'submit', command=lambda: answer_check(answer_entry.get()))
        bout.pack()
        
        btn = tk.Button(self, text='open game', command=run)
        btn.pack()

        
        def answer_check(entry):
            if entry == 'integer_three = 3':
                response_label['text'] = format_response('Yes')
            else: 
                response_label['text'] = format_response('No')

        response_label = answer = tk.Label(self)
        response_label.pack()

        boute = tk.Button(self, text = '<<', command = lambda: controller.up_frame('page_1'))
        boute.pack()

        bou = tk.Button(self, text = '>>', command = lambda: controller.up_frame('page_3'))
        bou.pack()


class page_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        self.id = controller.id
        self.entry1 = tk.StringVar()

        def run():
            os.system('python T3MC1.py')

        label = tk.Label(self, text = controller.id.get(), font = controller.titlefont)
        label.pack()
        message = tk.Label(self, text= """
Topic 3 - If/Elif/Else Statements

In some scenarios you will only want a set line(s) of code to execute if it meets a certain set of conditions.
The command “if” allows code to execute IF an expression is true. An if statement comes with a condition for something to be true.
The command “elif” is short for else if, and often comes after an “if” statement; if the condition for the previous “if” (or elif) statement is not met, it will move on to the elif branch and see if it meets the appropriate conditions to execute.
An elif statement comes with a condition for something to be true.
The command “else” comes after a sequence of if (and possibly elif statements); this branch will execute if it does not meet any of the conditions for the branches above.
An else statement DOES NOT come with a condition for something to be true.
Indenting and proper syntax/notation is important for these statements to execute properly. Refer to the examples below for the proper formatting.

Example 1:
number = 3
if number == 4:
	print(‘The number is 4!’)
elif number == 3:
	print(‘The number is 3!’)
else:
	print(‘The number is unknown.’)
Output: The number is 3!

IMPORTANT NOTE: The following code is for the practice in the answer box!

athlete = ‘Sidney Crosby’
if athlete == ‘Bob the builder’:
	print(athlete, ‘is a basketball player.’)
elif athlete == ‘Tom Brady’:
print(athlete, ‘is a football player.’)
elif athlete == ‘Cristiano Ronaldo’:
	print(athlete, ‘is a soccer player.’)
else:
	print(‘This person is unknown.’)
""", justify='left', font = controller.titlefont)
        message.pack()

        answer = tk.Label(self, text='For the code on the left (under example 2), type the terminal output:')
        answer.pack()

        answer_entry = tk.Entry(
            self, textvariable=self.entry1)
        answer_entry.pack()
        answer_entry.focus()

        bout = tk.Button(self, text = 'submit', command=lambda: answer_check(answer_entry.get()))
        bout.pack()
        
        btn = tk.Button(self, text='open game', command=run)
        btn.pack()

        def answer_check(entry):
            if entry == 'This person is unknown.':
                response_label['text'] = format_response('Yes')
            else: 
                response_label['text'] = format_response('No')

        response_label = answer = tk.Label(self)
        response_label.pack()

        bou = tk.Button(self, text = '<<', command = lambda: controller.up_frame('page_2'))
        bou.pack()

if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()
