from util import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('low', type=int)
parser.add_argument('high', type=int)

args = parser.parse_args()

for i in range(args.low,args.high+1):
    Process(target=compute_one, args=(i,)).start()
