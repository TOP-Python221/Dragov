a=int(input("Введите год: "))
if a%4==0 and a%100!=0:
    print("Високосный")
else:
    print("Невисокосный")