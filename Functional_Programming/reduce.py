# The function reduce(func, seq) continually applies the function func() to the sequence seq.
# It returns a single value.

f = lambda a,b: a if (a > b) else b
print reduce(f, [47,11,42,102,13])
