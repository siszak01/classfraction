import fractions

class Fractie:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fractie(newnum, newden)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fractie(new_num, new_den)
    def __invert__(self):
        return Fractie(self.den,self.num)


f1 = Fractie(1,4)
f2 = Fractie(1,2)
f1.show()

print("I ate", f1, "of the pizza")

f2.__str__()

str(f2)

print(f2)
#add
f3=f1+f2
print(f3)

f5 =fractions.Fraction(6, 8)
f6 =fractions.Fraction(1, 8)
#substract
z= f5-f6
print(z)


#invert
ReverseFun= ~f1
print(ReverseFun)







