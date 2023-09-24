class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calucurate_bmi(self):
        return round(self.weight/self.height**2, 2)


tanaka_bmi = BMI(height = 1.80, weight = 67.0)
sasami_bmi = BMI(height = 1.58, weight = 80.0)

print(tanaka_bmi.calucurate_bmi())
print(sasami_bmi.calucurate_bmi())