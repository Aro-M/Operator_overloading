class class_overloading:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other): #*
        return self.value * other.value

    def __truediv__(self, other): #/
        return self.value / other.value

    def __floordiv__(self, other): #//
        return self.value // other.value

    def __mod__(self, other): #%
        return self.value % other.value

    def __pow__(self, other): #**
        return self.value ** other.value

    def __rshift__(self, other): #>>
        return self.value >> other.value

    def __lshift__(self, other): # <<
        return self.value << other.value

    def __and__(self, other): # &
        return self.value & other.value

    def __or__(self, other): # |
        return self.value | other.value

    def __xor__(self, other): # ^
        return self.value ^ other.value

    def __lt__(self, other): # <
        return self.value < other.value

    def __gt__(self, other): # >
        return self.value > other.value

    def __le__(self,other): # <=
        return self.value <= other.value

    def __ge__(self,other): # >=
        return self.value >= other.value

    def __eq__(self,other): # ==
        return self.value == other.value

    def __ne__(self,other): # !=
        return self.value != other.value

    def __isub__(self, other): # -=
        self.value -=  other.value
        return self.value

    def __iadd__(self,other): # +=
        self.value += other.value
        return self.value

    def __imul__(self,other): # *=
        self.value *= other.value
        return self.value

    def __idiv__(self,other): #/=
        self.value /= other.value
        return self.value

    def __ifloordiv__(self, other):#//=
        self.value //= other.value
        return self.value

    def __imod__(self,other):  #%=
        self.value %= other.value
        return self.value

    def __ipow__(self, other): # **=
        self.value **= other.value
        return self.value

    def __irshift__(self,other): #>>=
        self.value >>= other.value
        return self.value

    def __ilshift__(self,other):  #<<=
        self.value <<= other.value
        return self.value

    def __iand__(self,other): # &=
        self.value &= other.value
        return self.value

    def __ior__(self,other): # |=
        self.value |= other.value
        return self.value

    def __ixor__(self, other): #^=
        self.value ^= other.value
        return  self.value

    def __neg__(self,other): #-
        self.value = self.value - other.value
        return self.value

    def __pos__(self,other): #+
        self.value = self.value + other.value
        return  self.value

    def __invert__(self): #~
        ~self.value
        return  self.value


obj1 = class_overloading(114)
obj2 = class_overloading(10)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 / obj2)
print(obj1 // obj2)
print(obj1 % obj2)
print(obj1 * obj2)
print(obj1 ** obj2)
print(obj1 >> obj2)
print(obj1 << obj2)
print(obj1 & obj2)
print(obj1 | obj2)
print(obj1 ^ obj2)
print()
print()
print()
print(obj1.__ifloordiv__(obj2))
print(obj1.__iadd__(obj2))
print(obj1.__neg__(obj2))
print(obj1.__ior__(obj2))
print(obj1.__ixor__(obj2))
print(obj1 == obj2)
print(obj1 != obj2)
print(obj1 > obj2)
print(obj1 < obj2)
print(obj1 >= obj2)
print(obj1 <= obj2)
print(obj1.__pos__(obj2))
print(obj1.__invert__())
print(obj1.__iand__(obj2))
print(obj1.__ilshift__(obj2))
print(obj1.__ipow__(obj2))
print(obj1.__irshift__(obj2))
print(obj1.__imod__(obj2))
print(obj1.__idiv__(obj2))
print(obj1.__imul__(obj2))
print(obj1.__isub__(obj2))
print(obj1.__imod__(obj2))

