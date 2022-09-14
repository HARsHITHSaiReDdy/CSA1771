import math

maximum, minimum = 1000, -1000

def alpha_beta(d, node, maxP, score, A, B):
    if(d == td) : 
        return score[node]
    if maxP : 
        best = minimum
        for i in range(0,2):
            value = alpha_beta(d+1, node*2+i, False, score, A, B)
            best = max(best, value)
            A = max(A,best)
            if B<=A : 
                break
        return best
    else :
        best = maximum
        for i in range(0,2):
            value = alpha_beta(d+1, node*2+i, True, score, A, B)
            best = min(best, value)
            B = min(B,best)
            if B<=A : 
                break
        return best

scr = []

x = int(input("Enter Total No. of leaf Nodes : "))
for i in range(x):
    y = int(input("Enter Leaf Node Values : "))
    scr.append(y)

td = math.log(len(scr), 2) #Finding Total Depth Of the Tree


d = int(input("Enter Depth Value : ")) # Depth Vlaue/Level-no from where the search begins
node = int(input("Enter Node Value : ")) # Node no. form where the search begins

print("The optimal value is ", alpha_beta(d, node, True, scr, minimum, maximum))
