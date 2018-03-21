# What is MyPY?
> MyPy is a standalone type checker which uses a bunch of the new features in 
> Python 3 to make the language more friendly to us type-lovers.
> -- http://ashaindlin.com/2016/02/MyPy-Tutorial/

Are _you_ a type lover?  Is it at all necessary?

Let's dive into typing hints and see...

-------------------------------------------------------------------------------
- TL;DR
- Examples
- Tricks
    - PyCharm plug
- Introducing into an existing project
    - Tips
- About covariance and contravariance
-------------------------------------------------------------------------------

# TL;DR

## MyPy will:
- give you "verified" documentation
- give you confidence when refactoring
- catch some bugs early

## will not:
- lint your code
- prevent logic bugs
- slow down your code, typing hints are ignored by the interpreter 


# Examples

- [Simple types](simple_types.ipynb)
- [Type inference](type_inference.py)
- [Collections covariance, built-in types](collections_covariance_buit_ins.py)
- [Collections covariance, classes](collections_covariance_classes.py)
- [None](none.py)
- [reveal_type](reveal_type.py)
- [Generators](generators.py)
- [Classes](classes_and_some_beers.py)
- [Duck type and classes, beer typing](classes_structural_subtyping_and_some_more_beers.py)
- [Generics](classes_generics.py)
- [Linting 1](linting_1.py)
- [Linting 2](linting_2.py)


# Tricks
- use typing module types instead of literals. Ex.: 
    ```
    # No    
    def Foo(bar: list) -> None:
        pass

    # Better
    from typing import List
    def Foo(bar: List) -> None:
        pass
        
    # Best: 
    def Foo(bar: List[int]) -> None:
        pass
    ```

- Use `--ignore-missing-imports` to remove messages about missing stubs.
- Use `--strict-optional`
- Use the docs: https://mypy.readthedocs.io/en/latest
    - But beware, it still has examples for Python type hinting into comments, so when you see:
    ```
    class A:
        def __init__(self) -> None:
            self.count = None  # type: int
    ```  
    think:
    ```
    class A:
        def __init__(self) -> None:
            self.count: int = None
    ```
 
## PyCharm plug
PyCharm has an integrated equivalent to MyPy. Many code inspections are displayed directly while editing.

I find that both work well together as MyPY can scan code _behind your back_ and run in the CI.

PyCharm code inspections also cover a lot (but not all) of what Pylint does. 
See linting_1.py and linting_2.py


# Introducing into an existing project

First, run  `mypy .` to scan all packages recursively. MyPy scans packages, make sure your sub folders have 
__init__.py package files.

If you get messages like `error: No library stub file for module 'pytest'`, try `--ignore-missing-imports`   
or append `# type: ignore`  after these imports.

Library stubs are typed libraries used by MyPy that define types for many known which do not have type hinting yet.

Fix any warnings. There should be none if the code has no type hinting yet.

Add the `--strict-optional` option and fix any new warning.

Then, add type hints gradually.

Later, check for basic consistency. Add the `--check-untyped-defs` option to your mypy arguments, and get that running
with no errors on the codebase. This option causes mypy to check every def in the codebase for internal consistency;
mypy can detect many classes of bugs and mistakes in your codebase, without your having written a single type
annotation!

When getting to 100% coverage, we can add `--disallow-untyped-defs`.


## Tips

- **Avoid using a guess-and-check approach when adding annotations.** In a partially annotated codebase, mypy will still
detect many classes of errors in annotations, but it can’t detect every error (since the inconsistency might be with
code you haven’t annotated yet). So you should make sure people writing annotations are actually understanding/tracing
the code, and that you code review the annotations just like actual code. We found writing one commit per large file (or
collection of related smaller files) to be a good commit discipline.

- Remember to annotate class variables!

- Use precise types where possible (e.g. avoid using Any ).

-- From http://blog.zulip.org/2016/10/13/static-types-in-python-oh-mypy


# About covariance and contravariance

Consider a class Employee with a subclass Manager. Now suppose we have a function with an argument annotated with
List[Employee]. Should we be allowed to call this function with a variable of type List[Manager] as its argument? Many
people would answer "yes, of course" without even considering the consequences. But unless we know more about the
function, a type checker should reject such a call: the function might append an Employee instance to the list, which
would violate the variable's type in the caller.

It turns out such an argument acts contravariantly, whereas the intuitive answer (which is correct in case the function
doesn't mutate its argument!) requires the argument to act covariantly. A longer introduction to these concepts can be
found on Wikipedia [wiki-variance] and in PEP 483; here we just show how to control a type checker's behavior.

**By default generic types are considered invariant in all type variables**, which means that values for variables 
annotated with types like List[Employee] must exactly match the type annotation -- no subclasses or superclasses of the 
type parameter (in this example Employee) are allowed.

