
import sys

from . import admin

def do(thing, frame):
    if thing.module is None or thing.method is None:
        pass
    else:
        method = getattr(sys.modules[thing.module], thing.method)
        method(thing.params, frame)