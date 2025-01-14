import random
def age_guesser():
    name = input("Please Enter Your Name: ")
    print(f'Hello {name}, this program will guess your age please press Y or N if the guess is correct or wrong.')
    User(name)
def random_guess():
    return random.randrange(15, 30)
def User(name):
    guess = random_guess()
    print(f'Is this your age: {guess}')
    user_input = input('Y/N: ')
    while True:
        if user_input == 'Y':
            print(f'{name} is {guess} years old')
            return False
        elif user_input == 'N':
            print('Rats!')
            User(name)
            return True
        else:
            return user_input
age_guesser()