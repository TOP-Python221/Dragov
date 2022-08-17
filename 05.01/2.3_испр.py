n=int(input("Введите число: "))
summ=0
for i in range(1,(n+1)):
    if n%i==0:
        summ+=i
print(f"Сумма делителей числа n:{summ}")