import plotly.plotly as py
import plotly.graph_objs as go



"""
int
consecutiveGCD(const
int & left, const
int & right);
double
avgConsecutiveGCD(const
int & input);
double
MDavg(int
n);
int
gcd(int
n, int
i);
"""


def main():
    nvals_list = []
    mdavg_data = []
    consec_div_data = []
    for i in range(1,1000,3):
        nvals_list.append(i)
        mdavg_data.append(mdavg(i))
        consec_div_data.append(avg_consecutive_gcd(i))

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

"""
int
consecutiveGCD(const
int & left, const
int & right)
{
int
divisions = 0;
int
min = (left > right? left:right);
for (int i = min; i > 0; i--)
    {
    if (left % min == 0)
    {
        divisions + +;
    if (right % min == 0)
    {
    divisions++;
return divisions;
}
}
}
return divisions;
}

def avgConsecutiveGCD(const int & input):
{
int
totalDivs = 0;
for (int i = 1; i <= input; i++)
    {
        totalDivs += consecutiveGCD(input, i);
    }
    return double(totalDivs) / double(input);
    }
"""


def mdavg(n):
    md = 0
    for i in range(1, n + 1):  #(int i = 1; i <= n; i++)
        md += gcd(n, i)

    return md / n


     #gcd returns number of modulo divisions for n

def gcd(n, i):
    if i == 0:
        return 0

    return gcd(i, n % i) + 1
