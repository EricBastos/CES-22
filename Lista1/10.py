import sys


def complex_add(cn1, cn2):
    return [cn1[0]+cn2[0], cn1[1]+cn2[1]]


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(complex_add([1, 2], [3, 4]) == [4, 6])
test(complex_add([-1, -2], [1, 2]) == [0, 0])
test(complex_add([0, 1], [1, 0]) == [1, 1])
test(complex_add([-1, -4], [1, 8]) == [0, 4])
