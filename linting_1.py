"""

Mypy can catch simple linting problems not directly related to types because
it still checks for parameter and return values

... continued into linting_2.py ...

"""

def i_see_things(obj1, obj2):
    pass


i_see_things(123)  # error: Too few arguments for "i_see_things"
                   # Pylint: E:  9, 0: No value for argument 'obj2' in function call (no-value-for-parameter)


# But a real linter will catch error like this:

def i_keep_forgetting():
    i = 123
    print(i)
    return

    print(i + 1)  # Pylint: W: 19, 4: Unreachable code (unreachable)
