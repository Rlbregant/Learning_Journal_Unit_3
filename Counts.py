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