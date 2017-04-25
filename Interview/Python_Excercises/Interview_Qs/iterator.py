So what is an iterator then? It's a stateful helper object that will produce the next value when you call next() on it. Any object that has a __next__() method is therefore an iterator. How it produces a value is irrelevant.

So an iterator is a value factory. Each time you ask it for "the next" value, it knows how to compute it because it holds internal state.

There are countless examples of iterators. All of the itertools functions return iterators. Some produce infinite sequences:

>>> from itertools import count
>>> counter = count(start=13)
>>> next(counter)
13
>>> next(counter)
14
Some produce infinite sequences from finite sequences:

>>> from itertools import cycle
>>> colors = cycle(['red', 'white', 'blue'])
>>> next(colors)
'red'
>>> next(colors)
'white'
>>> next(colors)
'blue'
>>> next(colors)
'red'
Some produce finite sequences from infinite sequences:

>>> from itertools import islice
>>> colors = cycle(['red', 'white', 'blue'])  # infinite
>>> limited = islice(colors, 0, 4)            # finite
>>> for x in limited:                         # so safe to use for-loop on
...     print(x)
red
white
blue
red
To get a better sense of the internals of an iterator, let's build an iterator producing the Fibonacci numbers:

>>> class fib:
...     def __init__(self):
...         self.prev = 0
...         self.curr = 1
...
...     def __iter__(self):
...         return self
...
...     def __next__(self):
...         value = self.curr
...         self.curr += self.prev
...         self.prev = value
...         return value
...
>>> f = fib()
>>> list(islice(f, 0, 10))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Note that this class is both an iterable (because it sports an __iter__() method), and its own iterator (because it has a __next__() method).

The state inside this iterator is fully kept inside the prev and curr instance variables, and are used for subsequent calls to the iterator. Every call to next() does two important things:

Modify its state for the next next() call;
Produce the result for the current call.
Central idea: a lazy factory
From the outside, the iterator is like a lazy factory that is idle until you ask it for a value, which is when it starts to buzz and produce a single value, after which it turns idle again.