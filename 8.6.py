#8.6
x=int(input("Nhập số km:"))
y=int(input("Nhập loại xe(chỗ):"))
z=int(input("Nhập số thời gian chờ (phút):"))
if y==4 and z==5 and x==20:
    print("tiền chờ free")
    print("Giá mở cửa: ",x*11000,"đồng")
    print("tiền di chuyển:",x*12100,"đồng")
    print("Tiền cước:",(x*12100+x*11000),"đồng")
elif y==4 and z>5 and x>=21:
    print("tiền chờ: ",z*800,"đồng")
    print("Giá mở cửa: ",x*11000,"đồng")
    print("tiền di chuyển:",x*10000,"đồng")
    print("Tiền cước:",(z*800+x*10000+x*11000),"đồng")
elif y==7 and z==5 and x==30:
    print("tiền chờ free")
    print("Giá mở cửa: ",x*13000,"đồng")
    print("tiền di chuyển:",x*14100,"đồng")
    print("Tiền cước:",(x*14100+x*13000),"đồng")
elif y==7 and z>5 and x>=31:
    print("tiền chờ: ",z*800,"đồng")
    print("Giá mở cửa: ",x*13000,"đồng")
    print("tiền di chuyển:",x*12000,"đồng")
    print("Tiền cước:",(z*800+x*13000+x*12000),"đồng")