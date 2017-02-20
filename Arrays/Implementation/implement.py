# An implementation of list as a dynamic array
import copy

class MyArray(object):
    def __init__(self):
        self.my_list = [None] * 10
        self.size = 0

    def add_element(self, element):
        if len(self.my_list) - self.size <= 0:
            for i in range(self.size):
                self.my_list.append(None)
        else:
            self.my_list[self.size] = element
            self.size += 1

    def access(self, index):
        if index > self.size:
            raise IndexError
        else:
            return self.my_list[index]

    def get_size(self):
        if self.size == 0:
            return 0
        else:
            return self.size + 1

    def remove(self, index):
        if index < self.size:
            element = self.my_list[index]
            self.my_list[index] = None
            temp = index
            while temp < self.size:
                self.my_list[temp] = self.my_list[temp + 1]
                self.my_list[temp + 1] = None
                temp += 1
            self.size -= 1
            return element
        else:
            raise IndexError


my_arr = MyArray()
print my_arr.get_size()
my_arr.add_element(10)
my_arr.add_element(20)
my_arr.add_element(30)
my_arr.add_element(40)
my_arr.add_element(50)
my_arr.add_element(60)
my_arr.add_element(70)
my_arr.add_element(80)
my_arr.add_element(90)
my_arr.add_element(100)
my_arr.add_element(110)
my_arr.add_element(120)
print my_arr.get_size()
print my_arr.access(0)
print my_arr.my_list
my_arr.remove(0)
print my_arr.my_list
print my_arr.get_size()
