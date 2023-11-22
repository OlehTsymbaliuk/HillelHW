def custom_max(*args):
    if not args:
        raise ValueError("No arguments provided")

    maximum = args[0]
    for arg in args[1:]:
        if arg > maximum:
            maximum = arg

    return maximum