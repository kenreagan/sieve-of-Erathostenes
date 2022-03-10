from math import ceil
from typing import Iterable
# sieve of erathostenes
def sieve(N: int)-> Iterable[int]:
	elem: List[bool] = [True] * N
	elem[0] = False
	elem[1] = False
	for x in range(2, ceil(N ** 0.5)):
		if elem[x]:
			for i in range(x*x, N, x):
				elem[i] = False
	return [i for i in range(len(elem)) if elem[i] == True]


print(sieve(10000000))
