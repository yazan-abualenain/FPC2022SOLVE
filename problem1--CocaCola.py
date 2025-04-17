from GetInputs import GetInputs
from rich import print
M,P,C = GetInputs([1,1,1])
totalPaid = M // P
totalFree = totalPaid // C
total = totalPaid + totalFree
print(total)

#Solved Successfully
# Time Complexity: O(1)
# Space Complexity: O(1)

