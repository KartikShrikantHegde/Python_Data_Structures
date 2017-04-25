class Negative(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message

def main():
    age = int(input("Type in your guess : Age of the Universe : "))
    print(age)
    try:
        if age <= 0:
            raise Negative("Please enter correct age")
    except Negative as e:
        print "Received error message as:", e.message

if __name__ == "__main__":
    main()


#
# def oops():
#     raise Negative()
#
#
# try:
#     age = int(input("Type in your guess : Age of the Universe : "))
#     print(age)
#     if age <= 0:
#         raise Negative()
# except ValueError:
#     print("Please make sure you type in an integer")
# except Negative:
#     print("Please make sure you type in a positive integer")
# except:
#     print("Somethings wrong!")
# finally:
#     print("finally!")
