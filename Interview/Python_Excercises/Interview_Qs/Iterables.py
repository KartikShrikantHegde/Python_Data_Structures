Iterables

When you create a list, you can read its items one by one. Reading its items one by one is called iteration:

>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:

>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
Everything you can use "for... in..." on is an iterable; lists, strings, files...

These iterables are handy because you can read them as much as you wish, but you store all the values in memory and this is not always what you want when you have a lot of values.