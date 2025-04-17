from GetInputs import GetInputs
from rich import print
from collections import deque
[N,C],W = GetInputs([2, 1])
if len(W) != N:
    raise ValueError("The number of weights must be equal to N.")
WC = deque(sorted(W))
RM = []
Ps = [[list(WC),sum(WC),[],0]]
for i in range(N):
    temp = WC.popleft()
    RM.append(temp)
    Ps.append([list(WC),sum(WC),[*RM],sum(RM)])
#print(f'{W=}, {N=}, {C=}, {Ps=}, {WC=}, {RM=}, {sum(WC)=}, {sum(RM)=}')
WC2 = sorted(W)
RM2 = []
for i in range(N):
    temp = WC2[-1]
    WC2.pop()
    RM2.append(temp)
    Ps.append([[*WC2],sum(WC2),[*RM2],sum(RM2)])
InBound = [i for i in Ps if i[1] <= C]
FinalItems =[]
for i in InBound:
    for j in i[2]:
        if j+i[1] <= C:
            CanGetBack = True
            break
        else:
            CanGetBack = False
    if not CanGetBack:
        FinalItems.append(i)
Final = sorted(FinalItems, key=lambda x: x[3],reverse=True)
Answer = Final[0][1]
print(Answer)
#Solved Successfully
#Time Complexity: O(N^2)
#Space Complexity: O(N)
