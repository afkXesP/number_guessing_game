import random
from datetime import datetime


def guess(num, target):
    if num > target:
        print(f'Incorrect! The number is less than {num}')
    elif num < target:
        print(f'Incorrect! The number is greater than {num}')
    else:
        return True
    return False


def main():
    print("""
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.
        """)

    print("""
        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        """)

    lvl = 0
    for _ in range(100):
        lvl = int(input('Enter your choice: '))
        if 1 <= lvl <= 3:
            break
        print('Please select a number from 1 to 3 that correspond to the difficulty level.')

    if lvl == 1:
        print('''
            Great! You have selected the Easy difficulty level.
            Let's start the game!
        ''')
        attempts = 10

    elif lvl == 2:
        print('''
            Great! You have selected the Medium difficulty level.
            Let's start the game!
        ''')
        attempts = 5
    else:
        print('''
             Great! You have selected the Hard difficulty level.
             Let's start the game!
                ''')
        attempts = 3

    target = random.randint(1, 100)
    flag = False
    start_time_point = datetime.now()

    while attempts > 0 and not flag:
        attempts -= 1
        num = int(input('Enter your guess: '))
        flag = guess(num, target)
    end_time_point = datetime.now()
    print(f'Congratulations! You guessed the correct number in {target} attempts.')
    print(f'Your playing time was: {end_time_point - start_time_point}')

    # print('Do you want to save the result?')
    # answer = input('Yes/No').lower()
    #
    # if answer == 'yes':
    #     with open('data.json', 'r') as file:
    #         data = file.readlines()
    #     print(data)


if __name__ == '__main__':
    main()
    game_plus = input('Would you like to play another game? (Yes/No)').lower()
    while game_plus.lower() != 'no':
        main()
        game_plus = input('Would you like to play another game? (Yes/No) ')
    print("Thanks for playing")


