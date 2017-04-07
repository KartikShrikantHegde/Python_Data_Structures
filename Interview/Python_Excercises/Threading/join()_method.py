import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def n():
    logging.debug('Starting')
    logging.debug('Exiting')


def d():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')


if __name__ == '__main__':
    t = threading.Thread(name='non-daemon', target=n)

    d = threading.Thread(name='daemon', target=d)
    d.setDaemon(True)

    d.start()
    t.start()

    # By default, join() blocks indefinitely.In our sample, join() blocks
    # the calling thread(main thread) until the threads(d / t) whose join()
    # method is called is terminated - either normally or through
    # an unhandled exception - or until the optional timeout occurs.

    # Note: Here main thread is calling the join method on 2 thread and thus waits
    # until they complete. Meanwhile it goes to wait state
    
    d.join()
    t.join()
