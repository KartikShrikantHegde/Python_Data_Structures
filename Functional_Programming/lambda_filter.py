# Lambda is used for quick function. If used over and over, defining function is better

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)


languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python",languages)


squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <=70, squares)