"""
Module 2 — Lesson 4: Functions
Student: [Gideon Fernandez]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Functions are reusable blocks of code that perform a specific task.
They help make programs easier to organize because we can write the
code once and use it many times. A function can receive information
through parameters and can send a result back using return.]


============================================
KEY VOCABULARY
============================================
- function: A reusable block of code that performs a specific task.
- parameter: A variable listed inside a function's parentheses.
- argument: The actual value given to a parameter when calling a function.
- return value: The result that a function sends back using return.
- function call: Using a function's name to make the function run.
- def: The keyword used to define a function in Python.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

def greet(name):
    return "Hello, " + name + "!"


student_name = "Gideon"
message = greet(student_name)

print(message)


def add_numbers(a, b):
    return a + b


result = add_numbers(10, 5)

print("The answer is:", result)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[One mistake I want to avoid is confusing parameters and arguments.
A parameter is the variable used when creating the function, while
an argument is the actual value given when calling the function.]


============================================

"""
