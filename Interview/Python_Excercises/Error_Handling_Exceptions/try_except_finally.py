while True:
   try:
      age = int(input("Type in your guess : Age of the Universe : " ))
      print(age)
      break
   except ValueError:
      print("Please make sure you type in an integer")
   except:
      break
   finally:
      print("age loop" )