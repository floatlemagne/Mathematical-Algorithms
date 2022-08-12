# Method for computing exponents; uses exponentiation by squaring method
def pow(a, n):
    if (n < 0):
        return pow(1/a, -n)
    elif(n == 0):
        return 1
    elif(n == 2):
        return a*a
    
    if(n % 2 == 0):
        return pow(a*a, n/2)
    else:
        return a*pow(a*a, (n-1)/2)

# Method for computing the square root of a number a; uses Heron's method
def sqrt(a):
    if(a < 0):
        return complex(0, sqrt(-a))
    elif(a == 0):
        return 0
    
    x = a
    
    while True:
        x0 = x
        x = (x + a/x)/2
        if is_precise(x0, x, 1e-14):
            break
    return x
  
# Method for computing the nth root of a number a; uses Newton's method
def root(n, a):
    if (n == 0):
        raise ValueError("Non-real error")
    elif(n < 0 or type(n) != int):
        raise ValueError("Invalid index")
    elif(n % 2 == 0 and a < 0):
        raise ValueError("Non-real error")
    elif(n == 1):
        return a

    x = a

    while True:
        x0 = x
        x = ((n-1)/n * x) + (a/n) * (1/pow(x, (n-1)))
        
        if is_precise(x0, x, 1e-14):
            break

    return x
  
# Method that determines whether the difference of two numbers is below a certain threshold value
def is_precise(x1, x0, epsilon):
    if epsilon <= 0:
        raise ValueError("Non-positive error")
    elif abs(x1-x0) < epsilon:
        return True
    return False
