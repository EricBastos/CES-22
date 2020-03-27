import sys


def reverse(s):
    revword = []
    size = len(s)
    while size > 0:
        revword += s[size-1]
        size -= 1
    return ''.join(revword)


def is_palindrome(s):
    return s == reverse(s)


def test(did_pass):

    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok".format(linenum)
    else:
        msg="Test at line {0} FAILED".format(linenum)
    print(msg)


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))
