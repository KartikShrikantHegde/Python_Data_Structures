def bob():
    me = "locally defined"    # Defined only in local context
    print me

bob()
print me     # Asking for a global variable
# The above will give you:

# locally defined
# Traceback (most recent call last):
#   File "file.py", line 9, in <module>
#     print me
# NameError: name 'me' is not defined
# While if you use the global statement, the variable will become available "outside" the scope of the function, effectively becoming a global variable.

def bob():
    global me
    me = "locally defined"   # Defined locally but declared as global
    print me

bob()
print me     # Asking for a global variable