synchronized statement in java:

public class Java {
    static private int count = 0;

    public void increment() {
       synchronized (this) {
          count++;
       }
    }
}
became :

import threading

class Java:
   cout = 0
   lock = threading.RLock()

   def increment():
       with Java.lock:
           Java.cout += 1
and synchronized method in Java:

public class Java {
    static private int count = 0;

    public synchronized void increment() {
        count ++;
    }
}
became:

import threading

def synchronized(method):
    """ Work with instance method only !!! """

    def new_method(self, *arg, **kws):
        with self.lock:
            return method(self, *arg, **kws)


    return new_method

class Java:
    count = 0
    lock = threading.RLock()

    @synchronized
    def incremenet(self):
        Java.count += 1