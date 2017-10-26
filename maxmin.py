"""
by travisbrady

A Python implementation of Daniel Lemire's Streaming Maximum-Minimum Filter
'Streaming Maximum-Minimum Filter Using No More than Three Comparisons per Element'
http://arxiv.org/abs/cs.DS/0610046
"""
from collections import deque
 
def supermaxmin(a, w):
    """
    # a: array to compute filter over
    # w: window width
 
    >>> a = [9, 0, 5, 1, 11, 23, 55, 4, 16, 47, 33]
    >>> w = 3
    >>> supermaxmin(a, w)
    ([9, 5, 11, 23, 55, 55, 55, 47, 47], [0, 0, 1, 1, 11, 4, 4, 4, 16])
    """
    maxfifo, minfifo = deque((0,)), deque((0,))
    lena = len(a)
    maxvalues = [None]*(lena-w+1)
    minvalues = [None]*(lena-w+1)
    for i in xrange(1, lena):
        if i >= w:
            maxvalues[i-w] = a[maxfifo[0]]
            minvalues[i-w] = a[minfifo[0]]
        if a[i] > a[i-1]:
            maxfifo.pop()
            while maxfifo:
                if a[i] <= a[maxfifo[-1]]:
                    break
                maxfifo.pop()
        else:
            minfifo.pop()
            while minfifo:
                if a[i] >= a[minfifo[-1]]:
                    break
                minfifo.pop()
        maxfifo.append(i)
        minfifo.append(i)
        if i == (w+maxfifo[0]):
            maxfifo.popleft()
        elif i == (w + minfifo[0]):
            minfifo.popleft()
        maxvalues[lena-w] = a[maxfifo[0]]
        minvalues[lena-w] = a[minfifo[0]]
    return maxvalues, minvalues
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
