import plotly.plotly as py
import plotly.graph_objs as go


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
