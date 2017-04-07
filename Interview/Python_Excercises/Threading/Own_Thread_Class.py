import threading

class MyThread(threading.Thread):

    def run(self):
        pass

if __name__ == '__main__':
    for i in range(3):
        t = MyThread()
        t.start()