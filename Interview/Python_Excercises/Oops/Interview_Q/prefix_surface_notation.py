str(x) -> an application program. This
prefix surface notation is implemented as x.__str__() under the hood.
A construct such as a+b may be implemented as a.__add__(b) or b.__radd__(a)
depending on the type of compatibility rules that were built into the class definitions
for objects a and b .