import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        some_function()
        print "Time it took to run the function:"
    return wrapper


@timing_function
def my_function():
    print("\nSum of all the numbers: " )


print(my_function())