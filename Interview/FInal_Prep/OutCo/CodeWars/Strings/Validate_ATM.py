def validate(pin):
    return len(pin) in (4,6) and pin.isdigit()

print validate('3123')