from util import *
    
for i in range(1,11):
    Process(target=compute_one, args=(i,)).start()
