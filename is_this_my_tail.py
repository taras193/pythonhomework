def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if tail == sub:
        return True
    else:
        return False