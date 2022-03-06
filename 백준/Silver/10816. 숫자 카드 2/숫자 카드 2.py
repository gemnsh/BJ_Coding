import sys
from collections import Counter
sys.stdin.readline()
N = sys.stdin.readline().split()
sys.stdin.readline()
M = sys.stdin.readline().split()
result = Counter(N)
print(' '.join(f'{result[i]}' if i in result else '0' for i in M))