from util import *
    
for i in range(41,51):
    Process(target=compute_one, args=(i,)).start()
