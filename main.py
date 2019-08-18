
import time
import bunch

import decision
import action

if __name__ == "__main__":
    frame = bunch.Bunch()
    frame.time = time.time()
    frame.admin_input = None

    while True:
        action.do(decision.make_next(frame), frame)
