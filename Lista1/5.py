import sys


def sum_elements(l):

    tot = 0
    for word in l:
        if word != "sam":
            tot += 1
        else:
            tot += 1
            break
    return tot


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(sum_elements(["eric","sam"])==2)
test(sum_elements(["a", "abc", "sam", "abcd"])==3)
test(sum_elements(["sam"])==1)
test(sum_elements(["eric", "teste"])==2)
test(sum_elements(["sam", "sam"])==1)
test(sum_elements(["sameric", "sam"])==2)
