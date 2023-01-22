# A class that makes an edge with 3 fields: 
# The number of cannibals, the numbers of missionaries, and which side we're on
class Edges:
    def __init__(self, mis, can, side):
        self.mis = mis
        self.can = can
        self.side = side

    # A string method that returns a solution in readable format when we print an
    # instance of the Edges class
    def __str__(self):
        return "(" + (str)(self.mis) + ", "+ (str)(self.can) +", " + self.side + ")"



# A function that checks if a passed in state we are going to go into is valid.
# returns true if valid, else returns false
def isvalid(start,eatCount):
    if start.mis < 0 or start.can < 0 or start.mis > 3 or start.can > 3:
        return False
    if start.mis < start.can or (3-start.can) < (3-start.mis) and start.side == "L":
        eatCount[0] +=1
        return False
    return True


# takes in a solution and prints out the path if its not redundant
def addSolutions(solutions, visited_stack):
    solution = tuple(visited_stack)
    for i in solutions:
      if(i[0] == visited_stack[0]):
        if(i[1] == visited_stack[1]):
          if(i[len(i)-2] == visited_stack[len(visited_stack)-2]):
            return
    if solution not in solutions:
        solutions.add(solution)
        print("Solution:")
        for i in solution:
           print(i, end = " ")
        print("\n")

# Takes in a an instance of the Edges class along with the path its on
# to explore possible solutions until we find them
def _dfs(start, visited_stack, solutions, eatCount,ancestorCount,totalCount):
    if not isvalid(start,eatCount):
        return
    if (start.mis, start.can, start.side) in visited_stack:
        ancestorCount[0]+=1
        return
    visited_stack.append((start.mis, start.can, start.side))
    totalCount[0]+=1
    if start.mis == 0 and start.can == 0 and start.side == "R":
        addSolutions(solutions, visited_stack)
        visited_stack.pop()
        return
    state = "L" if start.side == "R" else "R"
    if(state == "R"):
      if isvalid(Edges(start.mis, start.can-1,state),eatCount):
          _dfs(Edges(start.mis, start.can-1,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis-2, start.can,state),eatCount):
          _dfs(Edges(start.mis-2, start.can,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis-1, start.can,state),eatCount):
          _dfs(Edges(start.mis-1, start.can,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis-1, start.can-1,state),eatCount):
          _dfs(Edges(start.mis-1, start.can-1,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis, start.can-2,state),eatCount):
          _dfs(Edges(start.mis, start.can-2,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
    else:
      if isvalid(Edges(start.mis, start.can+1,state),eatCount):
          _dfs(Edges(start.mis, start.can+1,state),visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis+2, start.can,state),eatCount):
          _dfs(Edges(start.mis+2, start.can,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis+1, start.can,state),eatCount):
          _dfs(Edges(start.mis+1, start.can,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis+1, start.can+1,state),eatCount):
        _dfs(Edges(start.mis+1, start.can+1,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
      if isvalid(Edges(start.mis, start.can+2,state),eatCount):
          _dfs(Edges(start.mis, start.can+2,state), visited_stack, solutions,eatCount,ancestorCount,totalCount)
    visited_stack.pop()
    return

start = Edges(3, 3, "L")
visited_stack = []
solutions = set()
eatCount = [0]
ancestorCount = [0]
totalCount = [0]

_dfs(start, visited_stack, solutions, eatCount, ancestorCount, totalCount)


print("States that were repeated: " + str(ancestorCount[0]))
print("States where the cannibals ate the missionaries: " + str(eatCount[0]))
print("Total Legal States Searched: "+ str(totalCount[0]))


