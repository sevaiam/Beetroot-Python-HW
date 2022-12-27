# Створити декоратор який записує час та дату виконання функції. Вивід інформації має містити назву функції
# та дату і час у форматі hh:mm dd-mm-yy. Використати бібліотеку datetime.

from datetime import datetime


def start_time(func):
    def wrap():
        print(f'Function <{func.__name__}> started at:', datetime.now().strftime('%H:%m %d-%m-%y'))
        func()

    return wrap


@start_time
def main():
    print('hi')


if __name__ == "__main__":
    main()
