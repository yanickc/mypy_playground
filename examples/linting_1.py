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


# -----------------------------------------------------------------------------

from enum import Enum


class WeekDays(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


def is_it_tgif(day: WeekDays) -> bool:
    return day == WeekDays.FRIDAY


def day_score(day) -> float:
    if day == WeekDays.MONDAY:
        return 0.1
    elif day == WeekDays.TUESDAY:
        return 0.2
    elif day == WeekDays.WEDNESDAY:
        return 0.5
    elif day == WeekDays.THURSDAY:
        return 0.8
    elif day == WeekDays.FRIDAY:
        return 0.9

    # MyPy catches this because of the return value type :  error: Missing return statement


day = WeekDays.FRIDAY
print(day)  # WeekDays.FRIDAY
print(day.name)  # FRIDAY
print(day.value)  # 5

print(day_score(day))  # 0.9
print(is_it_tgif(day))  # True
