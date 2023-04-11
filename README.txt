The number of possible solutions PS for 'n' doesn't exceed the number of orderered sequences of 0-9 digits of length n.

This gives an estimate of PS = (n+9, 9) (n+9 choose 9)

Therefore the "changce" of such sequence giving an actual solution behaves as PS/10^{n}=(n+1/9)*(n+1/8)....(n+1)/10^n,

which behaves as n^10/10^n and rapidly approaches 0, which might serve as an explanation, why we didn't find any 
solutions past n=

