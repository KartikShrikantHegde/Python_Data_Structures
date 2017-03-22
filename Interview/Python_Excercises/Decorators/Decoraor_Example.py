Imagine we were using a web framework and have models with lots of currency related fields like price, cart_subtotal, savings etc. Ideally, when we output these fields, we would always prepend a "$". If we could somehow mark functions that produce these values in a way that would do that for us, that would be great.

This is exactly what decorators do. The function below is used to show the price with tax applied:

class Product(db.Model):

    name = db.StringColumn
    price = db.FloatColumn

    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like
        "7.0" for a 7% tax rate."""
        return price * (1 + (tax_rate_percentage * .01))

How can use the language to augment this function so that the return value has a "$" prepended? We create a decorator function, which has a useful shorthand notation: @. To create our decorator, we create a function which takes a function (the function to be decorated) and returns a new function (the original function with decoration applied). Here's how we would do that in our application:

def currency(f):
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))

    return wrapper

We include the 'args' and '*kwargs' as parameters to the wrapper function to make it more flexible. Since we don't know the parameters the function we're wrapping may take (and wrapper needs to call that function), we accept all possible positional (*args) and keyword (**args) arguments as parameters and "forward" them to the function call.

With currency defined, we can now use the decorator notation to decorate our price_with_tax function, like so:

class Product(db.Model):

    name = db.StringColumn
    price = db.FloatColumn

    @currency
    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like "7.0"
        for a 7% tax rate."""
        return price * (1 + (tax_rate_percentage * .01))

Now, to other code, it seems as though price_with_tax is a function that returns the price with tax prepended by a dollar sign. Notice, however, that we didn't change any code in price_with_tax itself to achieve this. We simply "decorated" the function with a decorator, giving it additional functionality.

Brief aside

One problem (easily solved) is that wrapping price_with_tax with currency changes its .__name__ and .__doc__ to that of currency, which is certainly not what we want. The functools modules contains a useful tool, wraps, which will restore these values to what we would expect them to be. It is used like so:

from functools import wraps

def currency(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))

    return wrapper
