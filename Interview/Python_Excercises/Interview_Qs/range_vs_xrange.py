range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange is a sequence object that evaluates lazily.

xrange() is more efficient because instead of generating a list of objects, it just generates one object at a time. Instead of 100 integers, and all of their overhead, and the list to put them in, you just have one integer at a time. Faster generation, better memory use, more efficient code.

You should favour range() over xrange() only when you need an actual list. For instance, when you want to modify the list returned by range(), or when you wish to slice it. For iteration or even just normal indexing, xrange() will work fine