
import plotly.offline as p_off
import plotly.graph_objs as go
from collections import Counter
from random import *
from numpy import arange,array,ones,asarray
from scipy import stats

def main():
    avg_input_list = []
    avg_input_list_euc = []
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

    min_primes_list = []

    for i in range(1, 100, 3):
        avg_input_list.append(i)
        avg_con_data.append(avg_consecutive_gcd(i))

    for i in range(1, 1000, 3):
        avg_input_list_euc.append(i)
        avg_euc_data.append(avg_euclids_gcd(i))

    for i in range(1, 1000):
        m = randint(1, 10000)
        n = randint(1, 10000)

        avg_prm_data.append(num_prime_ops(max(m, n), min(m, n)))

        min_primes_list.append(len(get_prime_factors(max(m, n), prime_gen(max(m, n)))))

    # kp1_max is the highest index of the fibonacci sequence we will generate
    kp1_max = 46
    fib_sequence = fibonacci_gen(kp1_max)

    for i in range(2, kp1_max + 1):

        fib_euc_data.append(md_euclids_gcd(fib_sequence[i], fib_sequence[i - 1]))

    trace_con = go.Scatter(x=avg_input_list, y=avg_con_data, name='Consecutive Integers')
    trace_euc = go.Scatter(x=avg_input_list_euc, y=avg_euc_data, name="Euclid's")
    p_off.plot({'data':  [trace_con], 'layout': {'title': 'Average Case Consecutive Integers', 'font': dict(size=16), 'yaxis': dict(title='avg divisions'), 'xaxis': dict(title='n')}}, filename='Average Case Consecutive.html')
    p_off.plot({'data':  [trace_euc], 'layout': {'title': "Average Case Euclid's Algorithm", 'font': dict(size=16), 'yaxis': dict(title='avg modulo divisions'), 'xaxis': dict(title='n')}}, filename='Average Case Euclids.html')

    slope, intercept, r_value, p_value, std_err = stats.linregress(min_primes_list, avg_prm_data)
    line = slope*asarray(min_primes_list)+intercept

    trace_prm = go.Scatter(x=min_primes_list, y=avg_prm_data, name="Prime Factorization", mode="markers")
    trend_line = go.Scatter(x=min_primes_list, y=line, name="Fit", mode="lines")
    p_off.plot({'data': [trace_prm, trend_line], 'layout': {'title': 'Prime vs Min', 'font': dict(size=16), 'yaxis': dict(title="comparison operations"), 'xaxis': dict(title="max size of prime lists")}}, filename='Prime vs Min.html')

    trace_euc = go.Scatter(x=fib_sequence, y=fib_euc_data, name="Euclid's Worst")
    p_off.plot({'data':  [trace_euc], 'layout': {'title': "Worst Case", 'font': dict(size=16), 'yaxis': dict(title="modulo divisoins"), 'xaxis': dict(title="m: fibonacci")}}, filename="Worst Case Eclid's.html")


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
    ops = 0
    for i in range(1, n + 1):
        ops += num_prime_ops(n, i)

    return ops / n


def num_prime_ops(m, n):
    operations = 0
    if m < n:
        minimum = n
    else:
        minimum = m

    m_primes = get_prime_factors(m, prime_gen(minimum))
    n_primes = get_prime_factors(n, prime_gen(minimum))

    i = 0
    j = 0
    while i < len(m_primes) and j < len(n_primes):
        if m_primes[i] == n_primes[j]:
            operations += 1
            i += 1
            j += 1
        elif m_primes[i] < n_primes[j]:
            operations += 2
            i += 1
        else:
            operations += 2
            j += 1

    return operations


main()

