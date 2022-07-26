
# Tribbles

![image](https://user-images.githubusercontent.com/15154218/180205712-0cb59e23-4656-4bbb-8593-e81205d018a5.png)


## Introduction

The USS Enterprise has a little trouble with Tribbles. 
The Tribbles are cute creatures, but they multiply too often.

You have N groups of tribbles, with M Tribbles per group. Every hour, one of the groups generates a new population of Tribbles with the same amount of the group, and those Tribbles can generate a new group or join one of the existing groups.

How many hours they need to have a total population of exactly K Tribbles?

## Examples
N=1 M=1 K=1
They need 0 hours, as there are already 1 Tribble as population.

N=1 M=1 K=2
They need 1 hour. The existing group generates a new group of 1, and this group can merge with the existing one or generates a new group, and the total population will be 2.

N=1 M=1 K=4
They need 2 hours. The existing group generates a new group of 1, that joins the existing group, so now we have 1 group with population 2. In the second hour this group generates a new group of 2, so we have 4 Tribbles.

N=2 M=2 K=12
They need 3 hours. 
Hour 0: Group 1 has 2 Tribbles, Group 2 has 2 Tribbles. Total population is 4.
Hour 1: Group 1 grow and join itself, so Group 1 has 4 Tribbles and Group 2 has 2 Tribbles. Total population is 6.
Hour 2: Group 1 grow and join itself, so Group 1 has 8 Tribbles and Group 2 has 2 Tribbles. Total population is 10.
Hour 3: Group 2 grow and join itself, so Group 1 has 8 Tribbles and Group 2 has 4 Tribbles. Total population is 12.

N=1 M=3 K=7
It's impossible

N=10 M=5 K=500
They need 10 hours

N=1234 M=13 K=13131313
They need 29 hours

## Challenge

Can you get the number of hours when N=33 M=35 and K=10670846278085

## Solution
For the solution, I will use the following notation:
$${Hours}=
\begin{pmatrix}
M \\
N \\
K
\end{pmatrix}
$$
First, let's assume that a group of Tribbles can't join or create a new group.

### Tribbles can't migrate
In this case, each group, individually, will grow as:

$$K = 2^{\alpha_1}·M+2^{\alpha_2}·M+...+2^{\alpha_N}·M = M·(2^{\alpha_1}+2^{\alpha_2}+...+2^{\alpha_N})  = M\sum_{i=0}^N 2^{\alpha_i}$$

Every group evolves individually as $2^n·M$, where n is the numbers of hours. For example, the evolution of a three Tribbles group in two hours will be $2^2·3=4·3=12$.

The last equation can be reduced as:

$$K = M\sum_{i=0}^N 2^{\alpha_i}$$

Looking at the las equation, we can assume two new things:
1. The total number of Tribbles we want to achieve at the end, should be divided into the initial number of Tribble that have each population, that means $M | K$.
2. Every problem can be reduced into $N$ groups of $1$ Tribble evolving to $K/M$:
$$
\begin{pmatrix}
M \\
N \\
K
\end{pmatrix} = 
\begin{pmatrix}
1 \\
N \\
K/M
\end{pmatrix}
$$



The problem then can be solved mathematically as find K as a sum of powers of 2, with the minimum power, using N terms.

Now let's consider the option that a group of Tribble, can migrate to another group or create a new one.

### Tribbles migration
For this, we have to consider that a term with $2^0$ means that group of Tribble don't change, so, every $\alpha_i = 0$ means no changes in that group. For example, consider two groups of one Tribble, and we want to have 6 Tribbles:
$$10 = 2^3 + 2^0 + 2^0$$
The last equiation means that two groups ($\alpha_1=0$ and $\alpha_2=0$) are not going to evolve, but the first one, will evolve three times (three hours $\rightarrow\alpha_0=3$).

So we can use the $2^0$ power to transfer other evolution to a group that never has evolved.
Let's call $Z_{k'}=\sum_1^{k'} 2^0$ for the groups that never evolve and don't have tranfers, so we can rewrite 10 as:
$$10=2^3+Z_2$$

Now let's consider the next problem: 2 groups of 1 Tribbles reaching a population of 6:
$$6=2^2+2^1$$
Group one evolves twice and group two evolves once. But evolving group 2 once, is the same that transfering the first evolution of the group 1 to two, so we can rewrite this as:
$$6=2^2+2^0(1+2^0)$$
The second term is the second group, with it initial value (1) and the transfer (1). So looking at this, we can write a number into:
$$K=2^\alpha+2^0(1+\sum_i 2^{p_i})+Z_{k'}$$
The only limitation is that $max\{p_i\}$ the maximum power value is $\alpha$, since we can't transfer a greater value from the first group than it's own value.

Now, let's called each individual term as: 

$$
A_1=2^\alpha \\
A_2'=\sum_i 2^{p_i} \\
A_3=Z_{k'}
$$

$$K=A_1+2^0(1+A_2')+A_3$$

Considerations
- $A_3$ will be $0$ if the number of groups are less than 2.
- A_2' will be $0$ if $K-(N-1)$ is a power of $2$, this means that we can get the number K just evolving one of the group.
- If $N < 2$, and K is not a power of $2$, we will create a new group at the begining, adding one hour at the end.

Assuming that 
- $[x]$ means to get the nearest integer rounding down the value of x.
- The function $b(x)$ means ${b}:X_{(10} \rightarrow X_{(2}$ transform a decimal to binary number.
- The function $o(x_{(2})$ transform the binary number $x$ in decimal as $2^pd_p$, where $d_p$ is the bit of $x$ at the position $p$. With this function, we can transform $x$ in a sum of powers of two.
- $|x|$ is the number of terms of a sum that have powers of two. In the case of $A_2': \\ A_2'=\sum_i 2^{p_i}\rightarrow |A_2'|=i$

We can get values for the last equations as:
$$
\alpha = [\log_2(K-(A_3+1))] \\
A_1=2^\alpha \\
A_2'=o(b(K-A_1-A_3-1)) \\
A_3=Z_{k'} \rightarrow k'=N-2 \\
$$

This is helpfull to know how groups evolved, but the problem only wants to know the exact number of hours, so we can reduce this as:
$${Hours}\space{of}
\begin{pmatrix}
1 \\
N \\
K
\end{pmatrix} = 
\alpha+|A_2'|$$

Remember that if a group was created at the begining, we have to add $+1$ to the last equation:
$$
\begin{pmatrix}
1 \\
N \\
K
\end{pmatrix} = 
1+\begin{pmatrix}
1 \\
N+1 \\
K
\end{pmatrix}
$$



### Solving the last problem
So last problem say to resolve 33 groups of 35 Tribbles to achieve a population of pmatrix.

$$
\begin{pmatrix}
35 \\
33 \\
10670846278085
\end{pmatrix} = 
\begin{pmatrix}
1 \\
33 \\
304881322231
\end{pmatrix}
$$

- First, $k'= 33 - 2 = 31 \rightarrow A_3=Z_{31}$
- Second, $\alpha=[\log_2(304881322231 -(31+1))]=[38.149...]=38 \rightarrow A_1 = 2^{38}$
- And finally: 
$A_2'=o(b(K-A_1-A_3-1))=o(b(30003415255))= o(11011111100010101111100100011011000)=2^0+2^1+2^2+2^4+2^6+2^7+2^{11}+2^{14}+2^{15}+2^{16}+2^{17}+2^{18}+2^{20}+2^{22}+2^{26}+2^{27}+2^{28}+2^{29}+2^{30}+2^{31}+2^{33}+2^{34} \\ 
\rightarrow |A_2'|=22$
$$
304881322231 = 2^{38}+2^0(1+A_2')+Z_{31}
$$

So the **solution** is: 
$$\begin{pmatrix}
1 \\
33 \\
304881322231
\end{pmatrix}=\alpha + A_2'=38+22=60\space{hours}$$.

## The code
This code has been written in Python 3.7.0, it is functional and it doesn't need any other extarnal resource.
```python
import math


# integer to binary
def i2b(n):
    binary = []

    if n == 0:
        binary.append(0)
    else:
        found = False

        while not found:
            binary.append(n % 2)
            c = int(n / 2)
            if c > 0:
                n = int(c)
            else:
                found = True

    return binary


def g(m, n, k):
    """
    For this case, using powers of 2, we know that:
        k = (2 ** alpha) + ((2 ** 0) * (1 + sum(i:0...t: 2 ** p_i))) + sum(i: 0...k', 2 ** 0)

    :param m: Number of tribbles per group
    :param n: Number of tribbles' groups
    :param k: Total population
    :return: Returns the number of hours it takes n groups of m Tribbles to form a total population of k
    """
    if (m * n) == k:
        return 0  # If m * n is k, we already have the population
    else:
        if m > 1 and k % m > 0:
            return -1  # if k cannot be divided by m, it is impossible to achieve the k population exactly
        elif m > 1:
            return g(1, n, k / m)  # reduce the problem
        else:
            if n > 1:
                a3 = n - 2
                alpha = int(math.log2(k - (a3 + 1)))
                a1 = 2 ** alpha
                a2 = k - a1 - a3 - 1
                a2_binary = i2b(a2)
                active_bits = sum([b for b in a2_binary if b == 1])
                return active_bits + alpha
            elif (k & (k - 1)) == 0:
                return math.log2(k)
            else:
                return 1 + g(m, n + 1, k)  # we add a new group, what means, 1 hour to create it


if __name__ == '__main__':
    # print(g(1, 1, 1))
    # print(g(1, 1, 2))
    # print(g(1, 1, 4))
    # print(g(2, 2, 12))
    # print(g(3, 1, 7))
    # print(g(5, 10, 500))
    # print(g(13, 1234, 13131313))
    print(g(35, 33, 10670846278085))

```
