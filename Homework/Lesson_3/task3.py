from random import randint, choice
import sys


def generate_task():
    operator = choice(['+', '-', '/', '*', '**'])
    a = randint(1, 100)
    b = randint(1, 100)
    match operator:
        case '+':
            print(f"{a} + {b} = ", end='')
            return a + b
        case '-':
            print(f"{a} - {b} = ", end='')
            return a - b
        case '/':
            print(f"{a} / {b} = ", end='')
            return a / b
        case '*':
            print(f"{a} * {b} = ", end='')
            return a * b
        case '**':
            print(f"{a} ** {b} = ", end='')
            return a ** b


def main():
    print(
        "Welcome to a math quiz!\nFor every correct answer you get a point, for every incorrect you lose two.\n"
        "You can exit anytime by typing 'exit'.")
    points = 0
    while True:
        task = generate_task()
        answer = input()
        if answer == 'exit':
            print(f"You've got {points} points so far. So sad to see you go!")
            break
        if int(answer) == task or float(answer) == task:
            points += 1
            print(f"Nice answer! You've got {points} points now!")
        else:
            points -= 2
            print(f"Better luck (and skill) next time. The answer was {task}. You've got {points} points.")


if __name__ == "__main__":
    main()
