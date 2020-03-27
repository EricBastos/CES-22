import sys


def sum_elements(l):

    tot = 0
    for element in l:
        if element % 2 == 1:
            tot += element
        else:
            break
    return tot


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(sum_elements([1, 3, 9, 10])==1+3+9)
test(sum_elements([1, 3, 10, 9, 11])==1+3)
test(sum_elements([2, 3, 9, 10])==0)
test(sum_elements([2, 4, 6, 1])==0)
test(sum_elements([1, 3, 9, 11])==1+3+9+11)
test(sum_elements([])==0)
test(sum_elements([1])==1)
test(sum_elements([2])==0)
