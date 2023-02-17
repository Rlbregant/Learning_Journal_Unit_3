def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    number = get_number()

    if number > 0:
        countdown(number)
    elif number < 0:
        countup(number)
    else:
        countdown(number)

main()

"""
Example 1: a positive number

Enter a number: 5
5
4
3
2
1
Blastoff!

Example 2: a negative number

Enter a number: -3
-3
-2
-1
Blastoff!

Example 3: zero

Enter a number: 0
Blastoff!

For input of zero, I chose to call the countdown function because space flight always counts down for launches. I 
could have called the countup function instead, but I thought it would be more interesting to see the countdown 
function in action for zero. 
"""