Don't do this:

value.key in dict.keys()
That--in Python 2, at least--creates a list containing every key. That gets more and more expensive as the dictionary gets larger, and performs an O(n) search on the list to find the key, which defeats the purpose of using a dict.

Instead, just do:

value.key in dict
which doesn't create a temporary list, and does a hash table lookup for the key rather than a linear search.

setdefault, as mentioned elsewhere, is the cleaner way to do this, but it's very important to understand the above.