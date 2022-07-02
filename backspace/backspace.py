from .kv import KV
import time

TIME_SLEEP = 0.7


class Backspace:
    def __init__(self):
        self.val = '\b'


backspace = Backspace()


def greeting():
    print("hello" + backspace.val + "world")


def n(num: int):
    if num < 0:
        raise ValueError("illegal input")
    return backspace.val * num


def printl(print_list, time_sleep=TIME_SLEEP):
    for i in print_list:
        len_i = len(i)
        print(i, end="")
        time.sleep(time_sleep)
        print(len_i * backspace.val, end="")


def loading():
    for i in range(10):
        print("-", end="")
        time.sleep(0.1)
    print("100%")
