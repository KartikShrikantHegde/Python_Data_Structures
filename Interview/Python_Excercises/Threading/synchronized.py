import time
import threading
from threading import Thread


def synchronized_method(method):
    outer_lock = threading.Lock()
    lock_name = "__" + method.__name__ + "_lock" + "__"

    def sync_method(self, *args, **kws):
        with outer_lock:
            if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)

    return sync_method

class Counter(object):
    def __init__(self):
        self.total = 0

    @synchronized_method
    def count(self):
        global total
        curr = total + 1
        time.sleep(0.1)
        total = curr

thread1 = Thread(target=Counter)
thread2 = Thread(target=Counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print total