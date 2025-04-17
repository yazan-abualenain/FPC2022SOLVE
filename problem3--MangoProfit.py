from GetInputs import GetInputs
from rich import print
N = GetInputs([1])[0]
listed = []
for i in range(1, N + 1):
    if N % i == 0:
        listed.append(i-1)
print(*listed, sep="  ")
#Solved Successfully
#Time Complexity: O(N)
#Space Complexity: O(N)