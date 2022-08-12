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

# Method for computing radicals
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif(n < 0):
        raise ValueError("Non-real error")
    return n*fact(n-1)
  
# Method for computing the sum of a geometric series
def geom_sum(sequence):
    if(len(sequence) <= 1):
        raise ValueError("Not a sequence")
    r = sequence[1]/sequence[0]
    return sequence[0] * (1-pow(r, len(sequence)))/(1-r)
  
# Method for computing the sum of a convergent geometric series
def geom_series(a, r):
    if r >= 1:
        raise ValueError("No sum")
    return a/(1-r)
