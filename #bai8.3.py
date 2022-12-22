print("Nhập vào số a: ")
a = int(input())
 
while True:
    if a == 0:
        print("Vui lòng nhập số a  ")
        a = int(input())
    else:
        break
print("Nhập vào số b: ")
b = int(input())
print("Nghiệm của phương trình là x = ", (-b / a))

