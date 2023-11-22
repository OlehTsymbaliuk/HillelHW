def custom_min(*args):
    if not args:
        raise ValueError("No arguments provided")

    minimum = args[0]
    for arg in args[1:]:
        if arg < minimum:
            minimum = arg

    return minimum