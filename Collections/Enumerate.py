# Enumerate is used similar to auto-increment for each occurrence. key will increment for every value
# and both key-value are stored just like hash

my_arr = [4,2,3,4,1,2]

for k,v in enumerate(my_arr):
    print k,v