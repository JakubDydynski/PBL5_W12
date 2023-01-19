#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string_parsing.h>

#include "shell.h"

#define TEST_CASES 12

#define TEST_ASSERT_EQUAL_INT(a, b, i) \
    do { \
        if (a != b) { \
            printf("Assertion failed: %d != %d at %d\n", a, b, i); \
        } \
        else printf("Good\n"); \
    } while (0)


void testcases(void);

int shell_function(int argc, char **argv)
{
    if (argc <= 2){
        printf("Pass at least one string and expected value\n");
        return -1;
    }

    for (int i = 1; i < argc; i+=2) {
        int ret = pair_parentheses(argv[i]);
        TEST_ASSERT_EQUAL_INT(ret, atoi(argv[ i+1]), i);
    }
    // testcases();

    return 0;
}

static const shell_command_t shell_commands[] = {{"Test", "Description", shell_function}};
char line_buf[SHELL_DEFAULT_BUFSIZE];

static char *test_str[TEST_CASES] = {
    "()[]{}", // 0
    "([{}])", // 1
    ")(",     // 2
    "(x+1]",  // 3
    "[x+1)",  // 4
    "(aef)",  // 5
    "([)]",   // 6
    "[]",     // 7
    "({)}",   // 8
    "",       // 9
    "][",     // 10
    "oaouh(uf"// 11
};

char c[] = {'[', ']', '{', '}', '(', ')'};

int returns[TEST_CASES] = {
    0,
    0,
    1,
    5,
    5,
    0,
    0,
    0,
    0,
    0,
    1,
    -1
};

void testcases(void)
{
    for (size_t i = 0; i < TEST_CASES; i++) {
        int ret = pair_parentheses(test_str[i]);
        TEST_ASSERT_EQUAL_INT(ret, returns[i], i);
    }
}

int main(void)
{


    puts("String parsing test application.");

    shell_run(shell_commands, line_buf, SHELL_DEFAULT_BUFSIZE);

    return 0;
}
