from .kv import KV
import time


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


kv = KV()


def kvf():
    pass


def loading():
    for i in range(10):
        print("-", end="")
        time.sleep(0.1)
    print("100%")
