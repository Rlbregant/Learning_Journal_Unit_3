# Runtime error
# Define a list of Firefly characters
characters = ['Mal', 'Zoe', 'Wash', 'Jayne', 'Inara', 'Kaylee', 'Simon', 'River', 'Book']

# Print the name of each character with a witty comment
for character in characters
    print("I aim to misbehave, " + character + "!")
"""
"C:\Users\Rosse\IdeaProjects\Battle Your Ships\venv\Scripts\python.exe" "C:/Users/Rosse/IdeaProjects/Learning Journal Unit 3/Runtime_Error.py"
File "C:\Users\Rosse\IdeaProjects\Learning Journal Unit 3\Runtime_Error.py", line 6
for character in characters
    ^
SyntaxError: expected ':'

To fix this error, we simply need to add the missing colon to the for statement:
"""

# Define a list of Firefly characters
characters = ['Mal', 'Zoe', 'Wash', 'Jayne', 'Inara', 'Kaylee', 'Simon', 'River', 'Book']

# Print the name of each character with a witty comment
for character in characters:# Added the missing colon here!
    print("I aim to misbehave, " + character + "!")

"""
The program consists of a simple for loop that iterates over a list of characters from the TV series Firefly. For each character, the program prints out a message that includes the character's name and a quote from the show.

The for loop is used to iterate over the characters in the firefly_characters list. In each iteration of the loop, the variable character is assigned to the next value in the list, starting with the first value. The loop then executes the indented block of code that follows the for statement, which prints out a message that includes the character's name and quote.

The output of the program shows that the loop is executing correctly, printing out a message for each character in the list. However, the program also raises a syntax error on the second line, which indicates that there is a problem with the syntax of the code.

The syntax error is caused by a missing colon after the for statement. In Python, a for loop must be followed by a colon, which indicates the start of the loop body. Because the colon is missing, the Python interpreter does not recognize the for loop and raises a syntax error.

To fix the syntax error, we need to add a colon after the for statement. Once the colon is added, the program runs without any errors and produces the expected output.
"""