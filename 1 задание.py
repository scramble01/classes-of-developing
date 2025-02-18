while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    D = b * b - 4 * a * c 

    if D < 0:
        print("В этом примере нету корней")

    if D == 0:
        w = 2 * a
        x1 = -b / w
    
        print("получился такой корень:")
        print(x1)
    if D > 0: 
    
        d2 = D**0.5
        d1 = d2
        w = -b + d1 
        x1 = w / 2 * a
        q = -b - d1
        x2 = q / 2 * a
    
        answer = x1,x2
    
    print("Получились такие корни: ")
    print(answer)
    
