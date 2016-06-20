# Hash_Function is handled internally

table = [0] * 10

def hash_function(x): return x % 10

def insert(table,input,value):
    table[hash_function(input)] = value
    print table


insert(table,41,'apple')
insert(table,93,'banana')
insert(table,13,'tangerine')


# For resolving collision

table = [[] for x in range(10)]

def insert(table,input,value):
    table[hash_function(input)].append((input,value))
    print table

insert(table,41,'apple')
insert(table,93,'banana')
insert(table,13,'tangerine')
