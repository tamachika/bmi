class BMI:
    def __init__(self, height, weight):
        self.value = round(weight / (height ** 2),2)
    def __str__(self):
        return f"{self.value}"


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print("tanaka")
print(tanaka_bmi)

print("sasami")
print(sasami_bmi)

#1