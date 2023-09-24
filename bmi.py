class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return round(self.weight/self.height**2, 2)


tanaka_bmi = BMI(height = 1.80, weight = 67.0)
sasami_bmi = BMI(height = 1.58, weight = 80.0)

 # tanakaさんの情報
print("tanaka")
print(tanaka_bmi.height,tanaka_bmi.weight)
print(tanaka_bmi.calculate_bmi())

# sasamiさんの情報
print("sasami")
print(sasami_bmi.height,sasami_bmi.weight)
print(sasami_bmi.calculate_bmi())