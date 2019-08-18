
import threading
import sys

class BackInput(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stack = []

    def run(self):
        while True:
            self._stack.append(input())

    def pop(self):
        return self._stack.pop()

back_input = BackInput()
back_input.start()

def read(_, frame):
    frame.admin_input = back_input.pop()

def write(params, frame):
    print(params.text)
0
def suspend(_, frame):
    sys.exit(0)