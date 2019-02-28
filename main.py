
import plotly.offline as p_off
import plotly.graph_objs as go
from collections import Counter


def main():
    avg_input_list = []
    avg_euc_data = []
    avg_con_data = []
    avg_prm_data = []

    # fibonacci x values are the m values (fib_sequence[i])

    # User testing mode
    print("User testing mode")

    n = int(input("(Task1) enter a value for n: "))
    print("MDavg: ", str(avg_euclids_gcd(n)))
    print("Davg: ", str(avg_consecutive_gcd(n)))

    k = int(input("(Task2) enter a value for k: "))
    fib_seq = fibonacci_gen(k+1)
    print("GCD(", str(fib_seq[k+1]), ", ", str(fib_seq[k]), ") = ", str(gcd(fib_seq[k+1], fib_seq[k])))

    m = int(input("(Task3) enter a value for m: "))
    n = int(input("(Task3) enter a value for n: "))

    print("GCD(", m, ", ", n, ") = ", str(prime_gcd(m, n)))

    print("Scatter plot mode")

    fib_euc_data = []

    for i in range(1, 100, 3):
        avg_input_list.append(i)
        avg_euc_data.append(avg_euclids_gcd(i))
        avg_con_data.append(avg_consecutive_gcd(i))
        avg_prm_data.append(avg_prime_gcd(i))


    # kp1_max is the highest index of the fibonacci sequence we will generate
    kp1_max = 100
    fib_sequence = fibonacci_gen(kp1_max)

    for i in range(2, kp1_max + 1):

        fib_euc_data.append(md_euclids_gcd(fib_sequence[i], fib_sequence[i - 1]))

    trace_con = go.Scatter(x=avg_input_list, y=avg_con_data, name='Consecutive Integers')
    trace_euc = go.Scatter(x=avg_input_list, y=avg_euc_data, name="Euclid's")
    trace_prm = go.Scatter(x=avg_input_list, y=avg_prm_data, name="Prime Factorization")
    p_off.plot({'data':  [trace_con, trace_euc, trace_prm], 'layout': {'title': 'Average Case', 'font': dict(size=16)}}, filename='Average Case.html')


    trace_euc = go.Scatter(x=fib_sequence, y=fib_euc_data, name="Euclid's Worst")
    p_off.plot({'data':  [trace_euc], 'layout': {'title': "Worst Case", 'font': dict(size=16)}}, filename="Worst Case Eclid's.html")


def consecutive_gcd(left, right):
    divisions = 0

    if left > right:
        minimum = left
    else:
        minimum = right

    for i in range(minimum, 0, -1):  # i = min; i > 0; i--)
        if left % minimum == 0:
            divisions += 1
            if right % minimum == 0:
                divisions += 1
                return divisions

    return divisions


def avg_consecutive_gcd(in_val):
    total_divs = 0
    for i in range(1, in_val, 1):  # (int i = 1; i <= in_val; i++):
        total_divs += consecutive_gcd(in_val, i)
    return total_divs/in_val


def md_euclids_gcd(n, i):
    if i == 0:
        return 0

    return md_euclids_gcd(i, n % i) + 1


def avg_euclids_gcd(n):
    md = 0
    for i in range(1, n + 1):
        md += md_euclids_gcd(n, i)

    return md / n


# gcd returns number of modulo divisions for n


def fibonacci_gen(n):
    fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[i-2] + fib_seq[i-1])

    return fib_seq


def prime_gen(k):
    primes = []
    is_prime = []
    for i in range(k+1):
        is_prime.append(True)

    p = 2
    while p*p <= k:

        if is_prime[p]:

            for i in range(p * p, k+1, p):
                is_prime[i] = False
        p += 1

    for i in range(2, k+1):
        if is_prime[i]:
            primes.append(i)

    return primes


def get_prime_factors(k, primes):
    prime_factors = []

    for i in range(len(primes)):  # for each element of primes if k mod p is 0 add it to the list
        if primes[i] > k:
            break
        while k % primes[i] == 0:
            k /= primes[i]
            prime_factors.append(primes[i])

    return prime_factors



# returns the gcd of n, i


def gcd(n, i):
    if i == 0:
        return n

    return gcd(i, n % i)



def prime_gcd(m, n):
    if m < n:
        minimum = n
    else:
        minimum = m

    m_primes = get_prime_factors(m, prime_gen(minimum))
    n_primes = get_prime_factors(n, prime_gen(minimum))
    intersect = list((Counter(m_primes) & Counter(n_primes)).elements())
    product = 1
    for i in intersect:
        product *= i

    return product


def avg_prime_gcd(n):
    md = 0
    for i in range(1, n + 1):
        md += prime_gcd(n, i)

    return md / n


main()

