import math
import sys


def is_prime(n):
    """
    Simple primality test
    """
    if n <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(is_prime(11))
test(not is_prime(35))
test(is_prime(2 ** 19 - 1))
test(not is_prime(2 ** 12 - 1))
test(not is_prime(1))
test(is_prime(2))
test(not is_prime(4))
test(is_prime(19990816)) # 16/08/1999, não é primo
