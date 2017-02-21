# An implementation of list as a dynamic array


class MyArray(object):
    def __init__(self):
        self.my_list = [None] * 10
        self.no_of_elements = 0

    def add_element(self, element):
        if len(self.my_list) - self.no_of_elements == 0:
            for i in range(self.no_of_elements):
                self.my_list.append(None)
            self.my_list[self.no_of_elements] = element
            self.no_of_elements += 1
        else:
            self.my_list[self.no_of_elements] = element
            self.no_of_elements += 1

    def access(self, index):
        if index > self.no_of_elements:
            raise IndexError
        else:
            return self.my_list[index]

    def get_size(self):
        return self.no_of_elements

    def remove(self, index):
        if index < self.no_of_elements:
            element = self.my_list[index]
            self.my_list[index] = None
            temp = index
            while temp < self.no_of_elements:
                self.my_list[temp] = self.my_list[temp + 1]
                self.my_list[temp + 1] = None
                temp += 1
            self.no_of_elements -= 1
            return element
        else:
            raise IndexError


my_arr = MyArray()
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

print my_arr.my_list
print my_arr.get_size()
print my_arr.remove(4)
print my_arr.my_list
print my_arr.get_size()