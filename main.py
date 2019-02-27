
import plotly.offline as p_off
import plotly.graph_objs as go


def main():
    nvals_list = []
    mdavg_data = []
    consec_div_data = []

    fibonacci_md_data = []
    #fibonacci x values are the m values (fib_sequence[i])

    for i in range(1, 100, 3):

        nvals_list.append(i)
        mdavg_data.append(mdavg(i))
        consec_div_data.append(avg_consecutive_gcd(i))

    trace_con = go.Scatter(x=nvals_list, y=consec_div_data, name='Consecutive Integers')
    trace_euc = go.Scatter(x=nvals_list, y=mdavg_data, name="Euclid's")
    p_off.plot({'data':  [trace_con, trace_euc], 'layout': {'title': 'Average Case', 'font': dict(size=16)}}, filename='Average Case.html')
    # , image='png')

    #kp1_max is the highest index of the fibonacci sequence we will generate
    kp1_max = 100
    fib_sequence = fibonacci_gen(kp1_max)
    for i in range(2, kp1_max + 1):
        fibonacci_md_data.append(gcd(fib_sequence[i], fib_sequence[i-1]))

    trace_euc = go.Scatter(x=fib_sequence, y=fibonacci_md_data, name="Euclid's Worst")
    p_off.plot({'data':  [trace_euc], 'layout': {'title': "Worst Case Euclid's", 'font': dict(size=16)}}, filename="Worst Case Euclid's.html")
    #, image='png')


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


def mdavg(n):
    md = 0
    for i in range(1, n + 1):
        md += gcd(n, i)

    return md / n
#gcd returns number of modulo divisions for n


def gcd(n, i):
    if i == 0:
        return 0

    return gcd(i, n % i) + 1


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
    while (p*p <= k):

        if (is_prime[p] == True):

            for i in range(p * p, k+1, p):
                is_prime[i] = False
        p += 1

    for i in range(k+1):
        if (is_prime[i] == True):
            primes.append(i)

    return primes


def get_prime_factors(k, primes):
    prime_factors = []

    for i in range(primes.len()): #for each element of primes if k mod p is 0 add it to the list
        if(primes[i] > k ):
            break
        if (k % primes[i] == 0):
            prime_factors.append(primes[i])

    return prime_factors


main()

