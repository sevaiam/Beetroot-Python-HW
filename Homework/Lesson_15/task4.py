# Task 4
# Custom exception
# Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
# functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend
# functionality for saving messages to file

class CustomException(Exception):

    def __init__(self, msg, message='Only lowercase allowed.'):
        self.msg = msg
        self.message = message
        super().__init__(self.message)
        with open('logs.txt', 'a') as log:
            log.write(f'\nError: {self} Input: <{self.msg}>')


try:
    msg_str = input('Enter a lowercase message: ')
    for i in msg_str:
        if not i.islower():
            raise CustomException(msg_str)
    print('Valid message.')
except CustomException as exception:
        print(f'! Invalid message. Error logged to logs.txt !')
