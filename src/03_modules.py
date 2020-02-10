import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
def sysArgs():
    for args in sys.argv:
        print(args)

sysArgs()

# Print out the OS platform you're using:
# YOUR CODE HERE

def curOS():
    print(sys.platform);

curOS()

# Print out the version of Python you're using:
# YOUR CODE HERE

def pyVersion():
    print(sys.version)

pyVersion()

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

def procID():
    print(os.getpid())

procID()

# Print the current working directory (cwd):
# YOUR CODE HERE

def currWD():
    print(os.getcwd())

currWD()

# Print out your machine's login name
# YOUR CODE HERE

def loginName():
    print(os.getlogin())

loginName()