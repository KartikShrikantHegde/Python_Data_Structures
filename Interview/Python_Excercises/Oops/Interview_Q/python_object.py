# Everything in Python is an object. This is unlike Java or C++ where there are
# "primitive" types that avoid the object paradigm.
#
# Primitive types are the basic types of data: byte , short , int , long , float , double , boolean , char . Primitive variables store primitive values.
#
# Reference types are any instantiable class as well as arrays: String , Scanner , Random , Die , int[] , String[] , etc.

a = 10
b = a
c = a

print id(a),id(b),id(c)


print id(a),id(b),id(c)

The problem comes from a misunderstanding of what variables are in Python. If you're used to most traditional languages, you have a mental model of what happens in the following sequence:

a = 1
a = 2
You believe that a is a memory location that stores the value 1,
then is updated to store the value 2. That's not how things work in Python.'
\ Rather, a starts as a reference to an object with the value 1,
then gets reassigned as a reference to an object with the value 2. Those two objects may continue to coexist even though a doesn't refer to the first one anymore; in fact they may be shared by any number of other references within the program.