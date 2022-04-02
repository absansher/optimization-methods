import math 
 
first = 0.0    
second = 6.0 
e = 0.4 
 
 
def f(x): 
    return 2*x**3 - 3*x**2 + 2*x -5 
     
     
y1 = f(first) 
y2 = f(second) 
 
 
if y2 * y1 >= 0: 
    print("voobshe net korney") 
else: 
    n = 1 
    x = (first+second)/2 
    y3 = f(x) 
    while (abs(y3) > e): 
        x = (first+second)/2 
        y3 = f(x); 
        if y1 * y3 < 0: 
            second = x 
            print( "x  = ",x)
        else: 
            first = x 
            n += 1 
            print( "x  = ",x)
    print( "Finally = ",x)
