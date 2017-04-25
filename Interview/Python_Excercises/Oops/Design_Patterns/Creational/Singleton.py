''' To create a single instance from a class.'''



# class Borg(object):
#     ''' Global variable or class variable '''
#
#     _shared_state = {}
#
#     def __init__(self):
#         self.__dict__ = self._shared_state


class Singleton(object):
    _shared_state = {}

    def __init__(self, **kwargs):
        # Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP="Hypertext trasnfer protocol")
y = Singleton(FTP="File trasnfer protocol")

print x
print y
