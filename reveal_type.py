# To find out what type MyPy infers for an expression anywhere in
# your program, wrap it in reveal_type.  MyPy will print an error
# message with the type; remove it again before running the code.

nodes = ['a', 'b', 'b']
stuff = {'something': [1, 2, 3], 'something_else': {}}


def f(obj1, obj2):
    pass


reveal_type(nodes)  # error: Revealed type is 'builtins.list[builtins.str*]'
reveal_type(stuff)  # error: Revealed type is 'builtins.dict[builtins.str*, typing.Collection*[builtins.int*]]'
reveal_type(f)  # error: Revealed type is 'def (obj1: Any, obj2: Any) -> Any'
