''' To postpone the object creation until it becomes absolutely necessary

So the client always interacts with proxy object until the resource intesnive object
  becomes available.

  Thus, its the responsibility of proxy to create resource intensive objects.
   The resource intensive object is expensive to be shared to everyone. '''

import time

class Producer(object):

    def produce(self):
        print "producer is working !"

    def meet(self):
        print "Producer is free now !"


# Less resource intensive object

class Proxy(object):
    def __init__(self):
        self.occupied = 'Yes'
        self.producer = None

    def produce(self):
        """ Check if producer is available """
        print "check if artist is available"

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()

        else:
            time.sleep(2)
            print "Producer is busy"


# instanciate the proxy

#  Producer is free now
p = Proxy()
p.produce()

# Make the producer busy
p.occupied = 'Yes'
p.produce()
