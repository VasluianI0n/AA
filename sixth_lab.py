import time
import matplotlib.pyplot as plt

from decimal import Decimal, getcontext

def calculate_pi_machin_like(n):
    getcontext().prec = n + 2

    pi = Decimal(0)
    sign = 1

    for k in range(n):
        numerator = (Decimal(4) / (8 * k + 1)) - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5)) - (Decimal(1) / (8 * k + 6))
        term = sign * numerator / (16 ** k)
        pi += term
        sign *= -1

    return str(pi)[:-1]

def calculate_pi_chudnovsky(n):
    getcontext().prec = n + 2
    
    pi = Decimal(0)
    k = 0
    
    while True:
        numerator = ((-1)**k) * (calculate_factorial(6*k)) * (Decimal(13591409) + Decimal(545140134)*k)
        denominator = (calculate_factorial(3*k)) * ((calculate_factorial(k))**3) * (Decimal(640320)**(3*k + Decimal(3)/Decimal(2)))
        
        term = Decimal(numerator) / Decimal(denominator)
        pi += term
        
        if abs(term) < 1e-15:  
            break
        
        k += 1
    
    return str(1/(pi*12))[:-1]

def calculate_factorial(n):
    factorial = Decimal(1)
    for i in range(2, n+1):
        factorial *= Decimal(i)
    return factorial

def calculate_pi_brent_salamin(n):
    getcontext().prec = n + 2

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)

    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * ((a - a_next) ** 2)
        a = a_next
        p *= 2

    pi = ((a + b) ** 2) / (4 * t)
    return str(pi)[:-1]

decimal_places = [10, 50, 100, 500]  

machin_like_times = []
chudnovsky_times = []
brent_salamin_times = []

for n in decimal_places:
    start_time = time.time()
    calculate_pi_machin_like(n)
    machin_like_times.append(time.time() - start_time)
    
    start_time = time.time()
    calculate_pi_chudnovsky(n)
    chudnovsky_times.append(time.time() - start_time)
    
    start_time = time.time()
    calculate_pi_brent_salamin(n)
    brent_salamin_times.append(time.time() - start_time)

plt.plot(decimal_places, machin_like_times, label="Machin-like Formula Algorithm")
plt.plot(decimal_places, chudnovsky_times, label="Chudnovsky Algorithm")
plt.plot(decimal_places, brent_salamin_times, label="Brent Salamin Algorithm")
plt.xlabel("Decimal Places")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time of Pi Approximation Algorithms")
plt.legend()
plt.show()