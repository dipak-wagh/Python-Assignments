class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


# Creating multiple objects
obj1 = Numbers(6)
obj2 = Numbers(7)

# Using first object
obj1.Factors()
print("Is Prime:", obj1.ChkPrime())
print("Is Perfect:", obj1.ChkPerfect())

print("---------------------")

# Using second object
obj2.Factors()
print("Is Prime:", obj2.ChkPrime())
print("Is Perfect:", obj2.ChkPerfect())
