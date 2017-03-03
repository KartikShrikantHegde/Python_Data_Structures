Sort -> IN place and thus orginal arr gets modified
Sorted -> original array doesnt change. you can use some var with sorted and use the variable

-------------------

x = [4,3,5,1]

x.sort()           -> In place sort

print x            -> original list is also modified

------------------

print x.sort()  -> this is wrong as sort() is in place sorting


print sorted(x) -> this gives sorted values to print, but original list x remains unchanged.
