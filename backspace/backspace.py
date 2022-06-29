from .kv import KV

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
