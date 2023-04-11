from util import *
    
for i in range(56,61):
    Process(target=compute_one, args=(i,)).start()
