import matplotlib.pyplot as plt
from decimal import *
# import decimal
import numpy as np
import math

EllyKey = 0
k = Decimal('-1.426465666768697071')
c = Decimal('-1.426465666768697070')
resultList = []
indexList = []
getcontext().prec = 2000
n = 100000

# result = Decimal(EllyKey).ln() * (1 - Decimal(EllyKey).ln())
result1 = Decimal('0')
result2 = Decimal('0')
for i in range(n):
    result1 = result1**2 + k
    result2 = result2**2 + c
    resultList.append(result1-result2)
    indexList.append(i)
print(resultList)
plt.axis([0, 10**6, -1, 1])
plt.grid()
plt.scatter(indexList, resultList, color='r')
plt.show()

