#9.3
import math
def BMI(a,b):
    return a/b*b
a=float(input("Nhập cân nặng(kg):" ))
b=float(input("Nhập chiều cao(m):"))
def phan_loai(BMI):
    if BMI <18.5:
        return "Bạn gầy quá"
    elif BMI <=25:
        return "Cơ thể của bạn bình thường"
    elif BMI >=25:
        return "Bạn bị thừa cân"
bmi = BMI(a,b)
print("Chi so co the cua ban la: ",bmi)
print(phan_loai(bmi))
