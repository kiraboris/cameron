
import importlib

submodules = {}

def do(thing, frame):
    if thing.module is None or thing.method is None:
        pass
    else:
        if not thing.module in submodules:
            submodules[thing.module] = importlib.import_module("." + thing.module, "action")
        method = getattr(submodules[thing.module], thing.method)
        method(thing.params, frame)