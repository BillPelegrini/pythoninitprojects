import sys

N = int(input())

pessoas = sys.stdin.readline().split()

lowest_pos = 0

for i in range(N): 
    if i == 0: 
        lowest = pessoas[i] 
        continue 
    if pessoas[i] < lowest: 
        lowest = pessoas[i] 
        lowest_pos = i 
        
print(lowest_pos + 1)