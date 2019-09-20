"""This is the starting point. It connects the core with a sensitive body."""

if __name__ == "__main__":
    import core
    import body
    body.create().life_loop(core.create())
