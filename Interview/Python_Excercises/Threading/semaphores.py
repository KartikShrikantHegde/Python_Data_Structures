Semaphores #

A semaphore is a more advanced lock mechanism. A semaphore has an internal counter rather than a lock flag, and it only blocks if more than a given number of threads have attempted to hold the semaphore. Depending on how the semaphore is initialized, this allows multiple threads to access the same code section simultaneously.

semaphore = threading.BoundedSemaphore()
semaphore.acquire() # decrements the counter
... access the shared resource
semaphore.release() # increments the counter
The counter is decremented when the semaphore is acquired, and incremented when the semaphore is released. If the counter reaches zero when acquired, the acquiring thread will block. When the semaphore is incremented again, one of the blocking threads (if any) will run.

Semaphores are typically used to limit access to resource with limited capacity, such as a network connection or a database server. Just initialize the counter to the maximum number, and the semaphore implementation will take care of the rest.

max_connections = 10

semaphore = threading.BoundedSemaphore(max_connections)
If you don’t pass in a value, the counter is initialized to 1.

Python’s threading module provides two semaphore implementations; the Semaphore class provides an unlimited semaphore which allows you to call release any number of times to increment the counter. To avoid simple programming errors, it’s usually better to use the BoundedSemaphore class, which considers it to be an error to call release more often than you’ve called acquire.

