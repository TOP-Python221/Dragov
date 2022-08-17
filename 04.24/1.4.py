a=int(input( "Введите число: "))

summa=0
proizved=1

while a>0:
    ost=a%10
    summa+=ost
    proizved*=ost
    a= a//10
print("Сумма цифр= ", summa)
print("Произведение цифр= ", proizved)    