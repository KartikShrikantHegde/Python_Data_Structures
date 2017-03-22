def is_even(value):
    """Return True if *value* is even."""
    return (value % 2) == 0

def count_occurrences(target_list, predicate):
    """Return the number of times applying the callable *predicate* to a
    list element returns True."""
    return sum([1 for e in target_list if predicate(e)])

my_predicate = is_even
my_list = [2, 4, 6, 7, 9, 11]
result = count_occurrences(my_list, my_predicate)
print(result)