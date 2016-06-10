#import urllib2

from urllib.request import urlopen
import time
def test():
    nf = urlopen("http://localhost:8080")
    start = time.time()
    page = nf.read()
    end = time.time()
    nf.close()
    result = end-start
    print(int(round(result * 1000)))
    #print(end-start)

if __name__ == "__main__":
    for i in range(0, 200):
        test()

