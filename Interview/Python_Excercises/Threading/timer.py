from threading import Thread
import time

def timer(name,delay,repeat):

    while repeat > 0:
        time.sleep(delay)
        print name + ": "+str(time.ctime(time.time()))
        repeat -= 1
    print "Timer "+name+" completed"


def main():
    t1 = Thread(target=timer("Timer1",5,5))
    t2 = Thread(target=timer("Timer2",1,5))
    t1.start()
    t2.start()

    print "Main Done"

if __name__ == '__main__':
    main()
