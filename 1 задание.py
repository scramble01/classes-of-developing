a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

D = b * b - 4 * a * c 

if D < 0:
    print("В этом примере нету корней")
    
else: 
    
    import cmath
    num = D 
    d1 = (cmath.sqrt(num))
    w = -b + d1 
    x1 = w / 2 * a
    q = -b - d1
    x2 = q / 2 * a
    
    answer = x1,x2
    
    print("Получились такие корни: ")
    print(answer)