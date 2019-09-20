"""The best mind in the world. =P"""

from concurrent.futures import ThreadPoolExecutor

class C:
    def name(self):
        return "Cameron"

    def admin_input(self, msg: str):
        print(msg)

def create():
    return C()