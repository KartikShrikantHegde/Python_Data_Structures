import uuid

class Project(object):
    __name = None
    __start_date = None
    __end_date = None
    __id = None
    __disc = None

    def __init__(self,name,start_date,end_date,disc):
        self.__id = uuid.uuid4()
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.disc = disc


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value





