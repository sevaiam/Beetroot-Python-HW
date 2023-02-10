# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel
# N or 'name' exists in the list, or "No" - in the other case.
#
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels: list):
        self.channels = channels
        self.current = 1

    def first_channel(self):
        self.current = 1
        print(f"Switched to first channel ({self.program()})")

    def last_channel(self):
        self.current = len(self.channels)
        print(f"Switched to last channel ({self.program()})")

    def turn_channel(self, ch):
        if ch <= len(self.channels):
            self.current = ch
            print(f"Switched to channel {self.current} ({self.program()})")
        else:
            print(f'Channel <{ch}> is out of range.')

    def next_channel(self):
        if self.current < len(self.channels):
            self.current += 1
        else:
            self.current = 1
        print(f"Switched to next channel ({self.program()})")

    def previous_channel(self):
        if self.current > 1:
            self.current -= 1
        else:
            self.current = len(self.channels)
        print(f"Switched to previous channel ({self.program()})")

    def current_channel(self):
        print(f"Current channel is {self.current} ({self.program()})")

    def is_exist(self, ch):
        if ch in self.channels or 1 <= int(ch) <= len(self.channels):
            return print(f'Channel <{ch}> exists.')
        else:
            return print(f'Channel <{ch}> DOES NOT exist.')

    def program(self):
        return self.channels[self.current - 1]


remote = TVController(CHANNELS)

remote.current_channel()
remote.first_channel()
remote.last_channel()
remote.turn_channel(1)
remote.next_channel()
remote.previous_channel()
remote.current_channel()
remote.is_exist(4)
remote.is_exist("BBC")
