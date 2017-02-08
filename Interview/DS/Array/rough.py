# a = 10
# b = a
# a = 12
# print b
#
# # tempNode.leftChild = self.rootNode
# # self.rootNode.remove(dataToRemove, tempNode)
# # print tempNode.leftChild.data
# # self.rootNode = tempNode.leftChild
#
# # print id(a), id(b)
# # b = 3
# #
# # print id(a), id(b)
# #
# # print b
#
# # x = 'foo'
# # print id(x)
# # y = x
# # print id(y)
# # print x # foo
# # y += 'bar'
# # print id(y)
# # print x # foo


# class Document:
#     def __init__(self, name):
#         self.name = name
#
#     x = 10
#     __my_var = 20
#
#     # def show(self):
#     #     raise NotImplementedError("Subclass must implement abstract method")
#
#
# class Pdf(Document):
#     def show(self):
#         return 'Show pdf contents!'
#
#
# class Word(Document):
#     def show(self):
#         return 'Show word contents!'
#
# a = Pdf('abc')
# print a._Pdf__my_var
#
# # documents = [Pdf('Document1'),
# #              Pdf('Document2'),
# #              Word('Document3')]
# #
# # for document in documents:
# #     print document.name + ': ' + document.show()

class Pdf(object):
    @staticmethod
    def show():
        return 'show    pdf contents!'

cc = Pdf()
print cc.show()
