from util import *
    
for i in range(11,21):
    Process(target=compute_one, args=(i,)).start()
