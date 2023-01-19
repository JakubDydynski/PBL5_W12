include ../Makefile.tests_common


RIOTBASE ?= $(CURDIR)/../..
WERROR = 0

CFLAGS += -I$(RIOTBASE)/sys/string_parsing/include/
USEMODULE += shell
USEMODULE += shell_commands
USEMODULE += string_parsing

SHOULD_RUN_KCONFIG ?=

include $(RIOTBASE)/Makefile.include

$(call target-export-variables.test)
