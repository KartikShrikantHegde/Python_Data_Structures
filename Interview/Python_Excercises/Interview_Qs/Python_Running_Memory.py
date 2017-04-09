# 1. When a Python executes a program, Python reads the .py into memory,
# 2. parses it in order to get a bytecode, then goes on to execute.
# 3. For imported programs, Python first checks to see whether
# there is a precompiled bytecode version, in a .pyo or .pyc,
# that has a timestamp which corresponds to its .py file. Python uses the bytecode version if any.
# Otherwise, it parses the module's .py file, saves it into a .pyc file, and uses the bytecode it just created.


# Python Virtual Machine (PVM)


# The PVM is the runtime engine of Python.
# Once our program has been compiled into byte code,
# it is shipped off for execution to Python Virtual Machine (PVM).
# The PVM is not a separate program. It need not be installed by itself. Actually,
# the PVM is just a big loop that iterates through our byte code instruction, one by one,
# to carry out their operations. 
# Technically it's just the last step of what is called the Python interpreter.