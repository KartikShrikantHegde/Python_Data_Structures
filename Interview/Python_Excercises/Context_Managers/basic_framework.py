# context manager is accompanied by -> try yield and finally
# its a slight modification of generators
# we use the decorator as well

@contextmanager
def sem_p(n):
    try:
        # setup code
        yield
    finally:
        # wrap-up code

