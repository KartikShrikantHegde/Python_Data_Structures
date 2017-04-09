Re-Entrant Locks (RLock) #

The RLock class is a version of simple locking that only blocks if the lock is held by another thread. While simple locks will block if the same thread attempts to acquire the same lock twice, a re-entrant lock only blocks if another thread currently holds the lock. If the current thread is trying to acquire a lock that it’s already holding, execution continues as usual.

lock = threading.Lock()
lock.acquire()
lock.acquire() # this will block

lock = threading.RLock()
lock.acquire()
lock.acquire() # this won't block
The main use for this is nested access to shared resources, as illustrated by the example in the previous section. To fix the access methods in that example, just replace the simple lock with a re-entrant lock, and the nested calls will work just fine.

lock = threading.RLock()

def get_first_part():
    ... see above

def get_second_part():
    ... see above

def get_both_parts():
    ... see above
With this in place, you can fetch either the individual parts, or both parts at once, without getting stuck or getting inconsistent data.

Note that this lock keeps track of the recursion level, so you still need to call release once for each call to acquire.