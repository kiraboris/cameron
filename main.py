
import time

import decision
import action

frame = object()
frame.time = time.time()
frame.admin_input = None

while True:
    action.do(decision.make_next(frame), frame)
