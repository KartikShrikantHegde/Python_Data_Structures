class Negative(Exception):
    pass


def oops():
    raise Negative()


try:
    age = int(input("Type in your guess : Age of the Universe : "))
    print(age)
    if age <= 0:
        print('calling ooops')
        oops()
except ValueError:
    print("Please make sure you type in an integer")
except Negative:
    print("Please make sure you type in a positive integer")
except:
    print("Somethings wrong!")
finally:
    print("finally!")
