
from utils import primesUpTo
from utils import numDistinctFactors
from utils import factorDictionary

primes = primesUpTo( 2000000 )
numFactors = numDistinctFactors( 28, primes )

def triangleDivisors( num ):

    factorDict1 = factorDictionary( num, primes )
    factorDict2 = factorDictionary( num + 1, primes )
    combinedDict = dict(factorDict1, **factorDict2)
    combinedDict[2] -= 1

    retVal = 1
    for f in combinedDict:
        retVal *= combinedDict[f] + 1
    return retVal

if __name__ == '__main__':
    triangleIndex = 1
    while True:
        if triangleDivisors ( triangleIndex ) > 200:
            print triangleIndex
            print  triangleIndex * (triangleIndex + 1) // 2
            break
        triangleIndex += 1


