# Generator object can be used only once. SO no reuse
# If called again its not gonna return anything, it has been already exhausted. Note
# it doesnt throw any exception
# If next method is called on generator object that has no value, stopiteration expection will
# be raised

# we can create new generator object to yield the values again

def gen(n):
    for i in range(1,n):
        if i % 2 == 0:
            yield i


# gen() -> returns a generator object assigned to gen_object variable

gen_object = gen(10)
# print gen_object.next()


# OR

# This for loop internally calls the next method on gen_object

for value in gen_object:
    print value

for value in gen_object:
    print value