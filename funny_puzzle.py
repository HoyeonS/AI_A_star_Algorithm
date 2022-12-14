import heapq




def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """

    distance = 0
    for i in range(len(from_state)):
       if(from_state[i] == 0):
           continue
       for j in range(len(to_state)):
           if(from_state[i] == to_state[j]):
               distance = distance + abs(i%3 - j%3) + abs((int)(i/3) - (int)(j/3))
    return distance


def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    succ_states = []
    
    for i in range(len(state)):
        if(state[i] == 0):
            if(i - 3 >= 0 and state[i-3] != 0):
                succ = state.copy()
                succ[i] = succ[i-3]
                succ[i-3] = 0
                succ_states.append(succ)
            if(i + 3 < len(state) and state[i+3] != 0):
                succ = state.copy()
                succ[i] = succ[i+3]
                succ[i+3] = 0
                succ_states.append(succ)
            if(i % 3 < 2 and state[i+1] != 0):
                succ = state.copy()
                succ[i] = succ[i+1]
                succ[i+1] = 0
                succ_states.append(succ)
            if(i % 3 > 0 and state[i-1] != 0):
                succ = state.copy()
                succ[i] = succ[i-1]
                succ[i-1] = 0
                succ_states.append(succ)




   
    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    OPEN = []
    CLOSED = []
    RECORD = []
    max_length = 0
    heapq.heappush(OPEN, (get_manhattan_distance(state), state, (0, get_manhattan_distance(state), -1)))
    while(True):
        if(len(OPEN) > max_length):
            max_length = len(OPEN)
        if(len(OPEN) == 0):
            print("Failure")
            break
        n = heapq.heappop(OPEN)
        CLOSED.append(n[1])
        RECORD.append(n)
        
        if(get_manhattan_distance(n[1]) == 0):
            print(state, " h=", get_manhattan_distance(state), " moves: 0", sep='')
            tmp = n
            AnsQueue = []
            while(tmp[1] != state):
                AnsQueue.append(tmp)
                tmp = RECORD[tmp[2][2]]
            for i in range(len(AnsQueue)):
                ans = AnsQueue[len(AnsQueue) - i - 1]
                print(ans[1]," h=",ans[2][1], " moves: ", ans[2][0], sep='')
                #print(RECORD.index(ans),ans)
            print("Max queue length:", max_length)
            break
        #print(n)
        for n_prime in get_succ(n[1]):
            h = get_manhattan_distance(n_prime)
            g = 1 + n[2][0]
            #print(n_prime, g, h)
            if(n_prime not in CLOSED):
                heapq.heappush(OPEN, (h + g, n_prime, (g, h, RECORD.index(n))))

    
        
        


if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([3, 4, 6, 0, 0, 1, 7, 2, 5])
    print()

    print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
