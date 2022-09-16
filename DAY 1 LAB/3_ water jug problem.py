
from collections import defaultdict

jug1, jug2, aim = 4, 3, 2

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):

	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True

	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		visited[(amt1, amt2)] = True

		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))

	else:
		return False

print("Steps: ")

waterJugSolver(0, 0)
#def pour(jug1, jug2):
    #max1, max2, fill = 5, 7, 4  #Change maximum capacity and final capacity
    #print("%d\t%d" % (jug1, jug2))
    #if jug2 is fill:
     #   return
    #elif jug2 is max2:
     #   pour(0, jug1)
    #elif jug1 != 0 and jug2 is 0:
     #   pour(0, jug1)
    #elif jug1 is fill:
     #   pour(jug1, 0)
    #elif jug1 < max1:
     #   pour(max1, jug2)
    #elif jug1 < (max2-jug2):
   #     pour(0, (jug1+jug2))
  #  else:
 #       pour(jug1-(max2-jug2), (max2-jug2)+jug2)
 
#print("JUG1\tJUG2")
#pour(0, 0)
