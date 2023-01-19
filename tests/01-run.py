import sys
import os
from testrunner import run
from random import rand

testcases = []

possibilities = [
    "()S",
    "S()",
    "(S)",
    "[]S",
    "S[]",
    "[S]",
    "\{\}S",
    "S\{\}",
    "\{S\}"
]

def create_good_testcases(string, n):
    for i in range(n):
        x = rand(0,9)
        s = possibilities[x]
        s.replace("S", string)
        print(s)

def testfunc(child):
    start = 'A'
    for i in range(100):
        create_good_testcases(start, rand(1,5))
    for testcase in testcases:
        child.sendline(testcase)
        child.expect_exact("Good\n")

if __name__ == "__main__":
    sys.exit(run(testfunc))
