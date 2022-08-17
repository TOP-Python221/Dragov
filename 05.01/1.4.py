k=ord(input("Введите букву исходной координаты короля: "))-96
l=int(input("Введите число исходной координаты короля: "))
m=ord(input("Введите букву конечной координаты короля: "))-96
n=int(input("Введите число конечной координаты короля: "))
if (k>=1 and k<=8 and l>=1 and l<=8 and m>=1 and m<=8 and n>=1 and n<=8)\
and((k+1==m and l==n)or(k-1==m and l==n)or(l+1==n and k==m)or(l-1==n and k==m)\
or(k+1==m and l+1==n)or(k-1==m and l-1==n)or(k+1==m and l-1==n)or(k-1==m and l+1==n)):
    print("Да")
else:
    print("Нет")
