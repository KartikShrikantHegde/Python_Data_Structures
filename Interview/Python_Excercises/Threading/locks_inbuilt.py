# For the same in python we don't have to add anything - it actually has this already built in - but instead of the synchronizedwith keyword.
#
# # Enter critical section
#
# with self.lock:
#
# # Do critical work
#
# # Exit critical section
#
#
# functionality of the "with" keyword can be defined
# for any class using the __enter__ and __exit__ methods.
#
# There is also a second advantage to using the with keyword over
# simply wrapping the critical section in self.lock.acquire() and self.lock.release().
# Using with ensures that the lock is always released,
# even if an exception occurs within the critical section.
# It will ensure that __exit__ is always called,
# much like the finally statement in a try block.

# LOCK Example:

import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func

