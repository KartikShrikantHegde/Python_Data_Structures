from threading import Thread

def f():
    print 'thread function'
    return

if __name__ == '__main__':
    for i in range(3):

        # Thread intialization
        t = Thread(target=f)
        # starting the thread
        t.start()
        # Error because you can start only once a thread object

        t.start()