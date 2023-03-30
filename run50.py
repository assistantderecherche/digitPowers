from util import *
    
if __name__ == '__main__':

    #for i in range(1,5):
    for i in range(41,51):
        Process(target=compute_one, args=(i,)).start()
