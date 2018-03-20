# Mypy can catch simple linting problems not directly related to types because
# it still checks for parameter and return values
# ...

def i_see_things(obj1, obj2):
    pass


i_see_things(123)  # error: Too few arguments for "f"
                   # Pylint: E:  9, 0: No value for argument 'obj2' in function call (no-value-for-parameter)


# ---

def i_keep_forgetting():
    i = 123
    print(i)
    return

    print(i + 1)  # Pylint: W: 19, 4: Unreachable code (unreachable)
