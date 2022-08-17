i=int(input("Введите число: "))
n=[]
while i%7==0:
    j=int(input("Введите число: "))
    n+=[j]
    if j%7!=0:break
print(i,",",''.join(str(n)))

# не смог вывести значения списка без скобок, применял join  



    
    
