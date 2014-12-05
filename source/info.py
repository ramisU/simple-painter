"""
Script containing info about the project.
"""

__info__ = {'author': 'Nelson Dos Santos', 'creation': '4.12.2014', 'updated':'5.12.2014', 'title':'Simple Painter'}


def show():
    """This functions shows __info__ in an ordered way"""
    for k, v in __info__.items():
        print("{0:<10}{1:<10}".format(k, v))
    print()


__type_errors__ = """In general, no type checking is done by any of the functions or methods in any of the modules or classes.
This was made for improving the performance of all the applications, and because so type checking (exceptions handling) seemed not to work.
Make sure you pass a valid parameter to all constructors, functions and methods.
"""
