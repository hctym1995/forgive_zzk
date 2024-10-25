import time
import tqdm

stop = 10
num = 230

def zzk():
    print('*'*num)
    for i in tqdm.tqdm(range(100), colour='green', desc='forgive zzk'):
        if i == stop:
            break
    print('*'* num)    
    
if __name__ == '__main__':
    zzk()
        