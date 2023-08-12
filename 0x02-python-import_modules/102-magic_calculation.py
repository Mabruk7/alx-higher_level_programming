#!/usr/bin/python3


def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
<<<<<<< HEAD
        return(sub(a, b))
=======
        return(sub(a, b))
>>>>>>> 8c85bb13fb928c7de227b9195451f43f43703102
