from random import randint


def main():
    points = 0
    print("Welcome to guessing game! You can always exit with 'exit' or cmd + C.")
    while True:
        number = randint(1, 10)
        answer = input("I'm thinking of a number from 1 to 10. Which number is it? ")
        if answer == 'exit':
            print(f"Wow, you've guessed {points} numbers! See you next time!")
            break
        elif answer.isdigit():
            if int(answer) == number:
                points += 1
                print(f"You guessed it! You've got {points} guesses total.")
            elif int(answer) > 10 or int(answer) < 1:
                print("I'm only thinking of numbers from 1 to 10")
            else:
                print(f'Nope, I was thinking of {number}')
        else:
            print("Please, only use digits.")


if __name__ == "__main__":
    main()
