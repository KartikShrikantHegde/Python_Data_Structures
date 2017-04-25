In python 3, range() does what xrange() used to do and xrange() does not exist.
If you want to write code that will run on both Python 2 and Python 3, you can't use xrange()

xrange returns an iterator. Therefore behind the scenes,
when looping it calls Next() method on the iterator.\ xrange is a
(generator)



It only keeps one number in memory at a time. range keeps the entire list of numbers in memory.

range creates a list of objecs, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange returns an object that evaluates lazily.

xrange() is more efficient because instead of generating a list of objects, it just generates one object at a time. Instead of 100 integers, and all of their overhead, and the list to put them in, you just have one integer at a time. Faster generation, better memory use, more efficient code.

You should favour range() over xrange() only when you need an actual list. For instance, when you want to modify the list returned by range(), or when you wish to slice it. For iteration or even just normal indexing, xrange() will work fine