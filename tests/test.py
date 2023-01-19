import sys
import os
from random import randint

# testcases = [
#     "Test \(\{\}\) 0\r\n",
#     "Test \(\{\)\} 3\r\n",
#     "Test \[\] 0\r\n",
#     "Test \]\[ -1\r\n",
#     "Test \[\[ -1\r\n",
#     "Test \]\] 1\r\n",
#     "Test \(\(\) -1\r\n",
#     "Test \)\) 1\r\n",
#     "Test \{\} 0\r\n",
#     "Test \{\{ -1\r\n",
#     "Test \}\} 1\r\n",
#     "Test \(\[\]\) 0\r\n"
# ]
testcases = []

possibilities = [
    "()S",
    "S()",
    "(S)",
    "[]S",
    "S[]",
    "[S]",
    "{}S",
    "S{}",
    "{S}"
]

braces = ['[', ']', '(', ')', '{', '}']


def create_good_testcases(string, n):
    if n == 0:
        return string.replace('S','')
    s = str()
    x = randint(0, 8)
    tmp = possibilities[x]
    s = string.replace("S", tmp)
    return create_good_testcases(s,n-1)


def create_bad_testcases(string, n):
    return f'{create_good_testcases(string, n)}{braces[randint(0, 5)]}'
    

def testfunc():
    for i in range(100):
        start = possibilities[randint(0,8)]
        print(create_good_testcases(start, randint(1,5)))
        print(create_bad_testcases(start, randint(1,5)))

if __name__ == "__main__":
    testfunc()