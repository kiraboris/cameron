
import time

def _every_msec(frame, every_msec):
    cur_time = time.time()
    elapsed = int((cur_time - frame.time) * 1000)
    return elapsed % every_msec

def _admin_decision(thing, frame):
    thing.module = "admin"
    if frame.admin_input is not None:
        lst = frame.admin_input.lower().strip().split()
        thing.method = lst[0]
        thing.params = lst[1:]
        frame.admin_input = None
        return True
    elif _every_msec(frame, 100):
        thing.method = "read"
        return True
    else:
        return False

def make_next(frame):
    thing = object()
    thing.module = None
    thing.method = None
    thing.params = []

    if _admin_decision(thing, frame):
        return thing

    return thing