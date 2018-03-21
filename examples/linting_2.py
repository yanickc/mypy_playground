"""

... but MyPy is not a true linter.

Here, it does not catch this hidden closure.

"""

LIST_OF_PRINTERS = []
for i in [1, 2, 3]:
    def printer():
        print(i)


    LIST_OF_PRINTERS.append(printer)

for func in LIST_OF_PRINTERS:
    func()

# But Pylint does:
#
# > pylint linting_2.py
# Using config file /Users/yanick/Documents/kaizen/dev/mypy_playground/.pylintrc
# ************* Module linting_2
# W:  9,14: Cell variable i defined in loop (cell-var-from-loop)
#
# -----------------------------------
# Your code has been rated at 8.57/10
