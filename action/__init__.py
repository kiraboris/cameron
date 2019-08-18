
import sys

from . import admin

def do(thing, frame):
    if thing is None:
        pass
    else:
        method = getattr(sys.modules[thing.module], thing.method)
        method(thing.params, frame)