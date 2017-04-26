''' To add additional functionality to an existing object dynamically
without using the subclasses for it

Lets say we want a simple message "Hello World" -> to blink


we use built in decorator using @ to accomplish this
'''

from functools import wraps


def make_blink(function):
    # ''' defines the decorator'''
    #
    # ''' pass in the function to decorate so that it becomes transparent'''

    @wraps(function)
    # ''' Define the inner function '''

    def decorator():
        ''' Grab the return value of the function being decorated '''

        ret = function()

        # ''' add new functionality to the function to decorate '''

        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here

@make_blink
def hello_world():
    return "Hello World"


print hello_world()
