pi = 3.14159265359

# Method for computing an approximation of a definite integral; uses Simpson's rule
def sim_int(a, b, f, n):
    if n % 2 != 0:
        raise ValueError("Parity error")
    if n <= 0:
        raise ValueError("Nonpositive error")
    
    dx = (b-a)/n
    sum = f(a) + f(b)

    for k in range (1, n):
        x = a + dx*k
        if k % 2 == 1:
            sum += 4*f(x)
        elif k % 2 == 0:
            sum += 2*f(x)

    sum = (1/3) * sum * dx

    return sum

# Method for computing a Riemann sum
def riemann_sum(a, b, f, n):
    if n <= 0:
        raise ValueError("Nonpositive error")

    dx = (b-a)/n
    sum = 0

    for k in range(1, n):
        sum += dx * f(a + dx*k)
    
    return sum

# Method for computing an approximation of a definite integral; uses Trapezoid rule
def trap_int(a, b, f, n):
    if n <= 0:
        raise ValueError("Nonpositive error")

    dx = (b-a)/n
    sum = 0

    sum = 0.5*f(a) + 0.5*f(b)
    
    for k in range(1, n):
        sum += f(a+k*dx)

    sum *= dx

    return sum

# Method for computing an approximation of the volume of a solid of revolution about the y-axis; uses Shell integration
def shell_int(a, b, f, g, n):
    if n <= 0:
        raise ValueError("Nonpositive error")
    
    dx = (b-a)/n
    sum = 0

    for k in range(1, n):
        x = a+dx*k
        sum += x * abs(f(x) - g(x)) * dx
    sum *= 2*pi

    return sum

# Method for computing an approximation of the volume of a solid of revolution about the x-axis; uses Disc integration
def disc_int(a, b, f, g, n):
    if n <= 0:
        raise ValueError("Nonpositive error")
    
    dx = (b-a)/n
    sum = 0

    for k in range(1, n):
        x = a+dx*k
        sum += (pow(f(x), 2) - pow(g(x), 2)) * dx
    sum *= pi
    
    return sum

# Method that determines whether the difference of two numbers is below a certain threshold value
def is_precise(x1, x0, epsilon):
    if epsilon <= 0:
        raise ValueError("Non-positive error")
    elif abs(x1-x0) < epsilon:
        return True
    return False
