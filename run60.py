from util import *
    
for i in range(51,61):
    Process(target=compute_one, args=(i,)).start()
