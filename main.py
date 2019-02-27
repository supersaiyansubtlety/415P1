import plotly.offline as p_off
import plotly.graph_objs as go


def main():
    nvals_list = []
    mdavg_data = []
    consec_div_data = []
    for i in range(1, 100, 3):
        nvals_list.append(i)
        mdavg_data.append(mdavg(i))
        consec_div_data.append(avg_consecutive_gcd(i))

    trace_con = go.Scatter(x=nvals_list, y=consec_div_data, name='Consecutive Integers')
    trace_euc = go.Scatter(x=nvals_list, y=mdavg_data, name="Euclid's")
    p_off.plot({'data':  [trace_con, trace_euc], 'layout': {'title': 'Average Case', 'font': dict(size=16)}}, image='png')


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


def gcd(n, i):
    if i == 0:
        return 0

    return gcd(i, n % i) + 1


main()
