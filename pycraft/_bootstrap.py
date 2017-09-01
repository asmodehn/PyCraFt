from __future__ import absolute_import, print_function, division, unicode_literals

import ast

"""
Bootstrapping a functional language
"""


# reflect to bytes (for humans)
def qut(sym):
    return bytes(sym)  # ascii first...


# reify to python
# Note : this could be "sent" to another process
# Note : types could be plugged in here...
def unq(lit, debug=False):
    if debug: print(lit)  # for debugging
    return ast.literal_eval(lit)


# apply
def app(fun, arg):
    return unq('(' + fun + ')' + '(' + arg + ')', True)


# abstract
def lam(arg, bod):
    return unq(ast.Lambda(arg, bod), True)


# # eval
# def evl()


def test_app_lam():
    """
    Verify that we have some kind of a lisp with this implementation, by examples:

    >>> qut(42)
    '42'

    >>> unq('42')
    42

    >>> qut(42) == unq('42')
    True

    >>> lam('x', 'x')
    42
    :return:
    """
    pass
    # TODO : formal or hypothesis test for lisp/pcf -like language capability
