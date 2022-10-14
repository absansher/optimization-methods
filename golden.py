import math 

first = 0.0
second = 6.0
e = 0.4

x = (first + second) / 2

def f(x):
    return 2*x**3 - 3*x**2 + 2*x -5

x1 = first + 0.382 * (second - first)
x2 = second - 0.382 * (second - first)
alfa = pow(x1, 2) + 2*x1
beta = pow(x2, 2) + 2*x2
while (True):   
    if (alfa < beta):
        second = x2
        break
    else:
        first = x1
        if (math.abs(second - first) < e):
            print (x, R)
        else:
            if b == x2:
                x2 = x1
                beta = alfa
                x1 = first + 0.382 * (second - first)    
                alfa = pow(x1, 2) + 2*x1
                
            if first == x1:
                x1 = x2
                alfa = f(x2)
                x2 = second - 0.382 * (second - first)
                beta = pow(x2, 2) + 2*x2
            break
