import os
from time import sleep


class Utils:
    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def sleep(seconds):
        sleep(seconds)
