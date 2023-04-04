from collections import Counter
import time

import multiprocessing as mp
from multiprocessing import Process

def sorter(s):
    l = s.split(',')
    n = len(l)
    s = n*10**(2*n)
    for i in range(n):
        val, howmany = [int(x) for x in l[i].split(":")]
        s += (val*10**(2*(n-i)-1) + howmany*10**(2*(n-i)))
    return s   


def gen_seq_str(N, upper_bound = 10):

    if upper_bound == 1:
        if N > 0:
            yield f"0:{N}"
        else:
            yield ''
    elif N == 1:
        for i in range(upper_bound):
            yield f"{i}:1"
    else:    
        for how_many in range(N + 1):
            if how_many == 0:
                for r in gen_seq_str(N, upper_bound - 1):
                    yield r
            else:
                for r in gen_seq_str(N-how_many, upper_bound - 1):
                    if r:
                        yield ",".join([r,f"{upper_bound - 1}:{how_many}"])
                    else:
                        yield f"{upper_bound - 1}:{how_many}"
                            

def pow_lookup_table(N):
    lkp = {}
    for d in range(10):
        for i in range(N+1):
            key = f"{d}:{i}"
            lkp[key] = i*d**N
            
    return lkp
    

def str2val(lkp, s):
    return sum([lkp[k] for k in s.split(",")])


def val2str(val):
    c = Counter(str(val))
    return ','.join([f"{x}:{y}" for x,y in sorted(c.items())])

            
def count_seq_strings(N, upper_bound = 10):
    return sum(1 for _ in gen_seq_str(N))


def printSizes(N, mode='gen'):
    
    if mode not in ['gen', 'list']:
        print(f"Unknown mode: {mode}")
        return
    
    sizes = []
    times = []
    for i in range(1,N+1):
        start_time = time.time()
        if mode == 'gen':
            sz = count_seq_strings(i)
        else:
            sz = len([*gen_seq_str(i)])
        
        dt = time.time() - start_time
        
        if i > 1:
            sz_ratio = sz/sizes[-1]  
            dt_ratio = dt/times[-1]
            print(f"{i = :2}\t\t{dt = :.1f}\t{sz_ratio = :.2f}\t\t{dt_ratio = :.2f}")
        else:
            print(f"{i = :2}\t\t{dt = :.1f}")
       
        sizes.append(sz)
        times.append(dt)
         
    print(f"\nSize,time ratios:\n")
    size_ratios = [sn/s for sn, s in zip(sizes[1:], sizes)]
    time_ratios = [tn/t for tn, t in zip(times[1:], times)]

    for sr, tr in zip(size_ratios, time_ratios):
        print(f"{sr:.2f}\t{tr:.2f}")
    
    print(f"\nSizes:\n")
    print(', '.join([str(s) for s in sizes]))

    return sizes

def computeSizeCombinatorics(n):
    
    sz = 1
    for i in range(1,10):
        sz *= (n/i+1)

    return round(sz)


def computeSizesCombinatorics(N):
    
    szs = []
    for n in range(2, N+1):
        szs.append(computeSizeCombinatorics(n))

    return szs
        
              
def printSizesList(N):
    printSizes(N, 'list')
        
        
def compute_for_range(n, N):
    
    if n < 1:
        print("Low range should be at least 1 ({n} given )")
        return
    
    if N - n > 2:
        print(f"\nComputing from {n} to {N-1}:\n")
    else:
        print(f"\nComputing for {N-1}:\n")
    
    start_time = time.time()
    
    for i in range(n, N):
        compute_one(i)
        
    time_taken = (time.time() - start_time)
    print(f"\n{time_taken = :.1f} seconds")

    
def compute_one(N):

    print(f"\nComputing for {N = }:")
    ts = time.time()
    lkp = pow_lookup_table(N)
    solutions = []
    count = 0
    mx_count = computeSizeCombinatorics(N)
    print_step = round(mx_count/10)
    for s in gen_seq_str(N):
        val = str2val(lkp, s)
        sval =  val2str(val)
        if s == sval:
            solutions.append(str(val))
        count+=1
        if N > 20 and count % print_step == 0:
            print(f"{N}: {round(count/print_step)*10}% done")


    if N > 20:
        print(f"{N}: 100% done")

    dt = time.time() - ts
    if len(solutions) > 0:
        print(f"n = {N},\t{dt:.1f} sec ---> {', '.join(solutions)}")
    else:
        print(f"n = {N},\t{dt:.1f} sec ... ") 

    
def compute(N=10):
    compute_for_range(1, N+1)


if __name__ == '__main__':

    for i in range(2,5):
        Process(target=compute_one, args=(i,)).start()
