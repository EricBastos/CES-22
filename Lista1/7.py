import sys


def sum_of_squares(l):

    tot = 0
    for element in l:
        tot += element*element

    return tot


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)
test(sum_of_squares([-1, 0, 1]) == 2)
test(sum_of_squares([-5, -5, -5]) == 75)
