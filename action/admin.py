
import multiprocessing
import sys

class InputProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self._stack = []

    def run(self):
        while True:
            self._stack.append(input())

    def pop(self):
        if self._stack:
            return self._stack.pop()
        else:
            return None

input_process = None

def read(_, frame):
    global input_process
    if not input_process:
        input_process = InputProcess()
        input_process.start()
    frame.admin_input = input_process.pop()
    print(frame.admin_input)

def write(params, frame):
    if params:
        print(" ".join(params))
0
def suspend(_, frame):
    input_process.terminate()
    sys.exit(0)