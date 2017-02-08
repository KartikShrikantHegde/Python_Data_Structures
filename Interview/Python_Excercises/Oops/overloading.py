class A(object):  # Remember the ``object`` bit when working in Python 2.x

    def stackoverflow(self, i=None):
        if i is None:
            print 'first form'
        else:
            print i

ob = A()
ob.stackoverflow()
ob.stackoverflow(2)