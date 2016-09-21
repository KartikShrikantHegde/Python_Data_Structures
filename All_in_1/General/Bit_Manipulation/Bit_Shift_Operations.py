'''This operation is mathematically equivalent to floor dividing and multiplying by 2 (respectively)
 for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s
  left or right by the specified number of slots.

Note that you can only do bitwise operations on an integer.
Trying to do them on strings or floats will result in nonsensical output! '''

shift_right = 0b1000
shift_left = 0b1

# This shifts the digits by 2 places.

# Your code here!
shift_right=shift_right>>2

# This adds 2 zeros to by shifting the digits to left by 2 places.

shift_left=shift_left<<2

print bin(shift_right)
print bin(shift_left)