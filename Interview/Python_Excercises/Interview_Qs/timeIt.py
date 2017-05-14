# Tool for measuring execution time of small code snippets.
# The program is passed as an argument to timer.timeit function

# timeit function creates a Timer object -> which can be used to call timer function which is useful
# for operations related to time

import timeit
x = timeit.timeit()
print x.timeit('"-".join(str(n) for n in range(100))', number=10000)