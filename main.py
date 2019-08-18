
import decision
import action

frame = None
while True:
    action.do(decision.make_next(frame))
