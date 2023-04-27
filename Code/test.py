from decimal import *

getcontext().prec = 1000
NumericEllyKey = '6465666768'
print(Decimal('-1.42') - Decimal(str(NumericEllyKey)) / (Decimal('10')**(len(NumericEllyKey)+2)))
