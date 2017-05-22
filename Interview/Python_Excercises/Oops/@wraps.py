If using a decorator always meant losing this information about a function, it would be a serious problem.
That's why we have functools.wraps. This takes a function used in a decorator and adds the' \
    ' functionality of copying over the function name, docstring, arguments list, etc. And since wraps is itself a decorator, the following code does the correct thing:


This is perticularly helpful during the debugging decorator functions.