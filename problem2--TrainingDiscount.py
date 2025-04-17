from GetInputs import GetInputs
from rich import print
V,D,S = GetInputs([1,1,1])
Dratio = 1
if len(S) != D:
    raise Exception("The number of steps list items must be equal to the number of days")
if S[1] != 2* S[0] or S[0]<200:
    print(f"Discount = {0.0}\nNet Cost = {float(V)}")
else:
    for i in range(0, D):
        if i + 1 < len(S):
            if S[i+1] == 2 * S[i]:
                Dratio += 1
            else:
                break
    Discount = float((Dratio / D) * V)
    NetCost = float(V - Discount)
    print(f"Discount = {Discount}\nNet Cost = {NetCost}")


#Solved Successfully
#Time Complexity: O(n) 
#Space Complexity: O(1)