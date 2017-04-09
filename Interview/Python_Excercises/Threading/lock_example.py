Problems with Simple Locking #

The standard lock object doesn’t care which thread is currently holding the lock; if the lock is held, any thread that attempts to acquire the lock will block, even if the same thread is already holding the lock. Consider the following example:

lock = threading.Lock()

def get_first_part():
    lock.acquire()
    try:
        ... fetch data for first part from shared object
    finally:
        lock.release()
    return data

def get_second_part():
    lock.acquire()
    try:
        ... fetch data for second part from shared object
    finally:
        lock.release()
    return data
Here, we have a shared resource, and two access functions that fetch different parts from the resource. The access functions both use locking to make sure that no other thread can modify the resource while we’re accessing it.

Now, if we want to add a third function that fetches both parts, we quickly get into trouble. The naive approach is to simply call the two functions, and return the combined result:

def get_both_parts():
    first = get_first_part()
    second = get_second_part()
    return first, second
The problem here is that if some other thread modifies the resource between the two calls, we may end up with inconsistent data. The obvious solution to this is to grab the lock in this function as well:

def get_both_parts():
    lock.acquire()
    try:
        first = get_first_part()
        second = get_second_part()
    finally:
        lock.release()
    return first, second
However, this won’t work; the individual access functions will get stuck, because the outer function already holds the lock. To work around this, you can add flags to the access functions that enables the outer function to disable locking, but this is error-prone, and can quickly get out of hand. Fortunately, the threading module contains a more practical lock implementation; re-entrant locks.


