### PROBLEM:

Find numbers **X** such that if **X** has **n** digits, then 

		sum_{digit d} d^n == X

### DONE:

Experimentally checked n up to 60. The solutions can be found in report.txt

### ANALYSIS:

For given **n** (number of digits), number of possible solutions (denoted here **PS(n)**)
doesn't exceed the number of orderered sequences of 0-9 digits of length n.

This gives an upper bound estimate for PS(n) as:

		PS(n) = (n+9, 9) reads as (n+9 choose 9)

Therefore "chances" of such sequence giving an actual solution behave as:

		PS/10^{n}=(n+1/9)*(n+1/8)....(n+1)/10^n,

which behaves as n^10/10^n and therefore rapidly approaches 0 as n grows.

This might serve as an explanation, why **we didn't find any solutions past n = 39**

Also, note that the number of variants the program considers grows as n^10, which is ultimately much better than the straightforward 10^n.
