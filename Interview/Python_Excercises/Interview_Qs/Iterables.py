most containers are also iterable. But many more things are iterable as well. Examples are open files, open sockets, etc. Where containers are typically finite, an iterable may just as well represent an infinite source of data.

An iterable is any object, not necessarily a data structure, that can return an iterator (with the purpose of returning all of its elements). That sounds a bit awkward, but there is an important difference between an iterable and an iterator. Take a look at this example:

>>> x = [1, 2, 3]
>>> y = iter(x)
>>> z = iter(x)
>>> next(y)
1
>>> next(y)
2
>>> next(z)
1
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list_iterator'>
Here, x is the iterable, while y and z are two individual instances of an iterator, producing values from the iterable x. Both y and z hold state, as you can see from the example. In this example, x is a data structure (a list), but that is not a requirement.

NOTE:
Often, for pragmatic reasons, iterable classes will implement both __iter__() and __next__() in the same class, and have __iter__() return self, which makes the class both an iterable and its own iterator. It is perfectly fine to return a different object as the iterator, though.

Finally, when you write:

x = [1, 2, 3]
for elem in x:
    ...
This is what actually happens:



When you disassemble this Python code, you can see the explicit call to GET_ITER, which is essentially like invoking iter(x). The FOR_ITER is an instruction that will do the equivalent of calling next() repeatedly to get every element, but this does not show from the byte code instructions because it's optimized for speed in the interpreter.

>>> import dis
>>> x = [1, 2, 3]
>>> dis.dis('for _ in x: pass')
  1           0 SETUP_LOOP              14 (to 17)
              3 LOAD_NAME                0 (x)
              6 GET_ITER
        >>    7 FOR_ITER                 6 (to 16)
             10 STORE_NAME               1 (_)
             13 JUMP_ABSOLUTE            7
        >>   16 POP_BLOCK
        >>   17 LOAD_CONST               0 (None)
             20 RETURN_VALUE

