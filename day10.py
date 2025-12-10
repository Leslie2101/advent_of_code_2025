def getButtonVal(pos):
    val = 0

    for p in pos:
        val += 2**int(p)
    return val 


def getPatternVal(pattern):
    val = 0

    for i in range(len(pattern)):
        if pattern[i] == "#":
            val += 2**i        
    return val 



from collections import defaultdict, deque
def getMinPresses(patternVal, buttonVals):

    visited = set()
    buttonValPairs = [(buttonVal, 1) for buttonVal in buttonVals]
    queue = deque(buttonValPairs)

    while queue:
        val, count = queue.popleft()

        if val in visited:
            continue

        if val == patternVal:
            return count 

        visited.add(val)

        for button in buttonVals:
            newVal = val ^ button
            if newVal not in visited:
                queue.append((newVal, count + 1))
        
    return -1 




with open("inputTxt.txt", "r") as f:
    lines = f.readlines()
    partA = 0
    for line in lines:
        pattern, values = line.split(maxsplit=1)
        pattern = pattern.strip("[]")
        patternVal = getPatternVal(pattern)

        buttons = values.split()[:-1]
        buttonVals = []
        for button in buttons:
            button = button.strip("()")
            poss = button.split(",")
            buttonVal = getButtonVal(poss)
            buttonVals.append(buttonVal)

        minPress = getMinPresses(patternVal, buttonVals)
        partA += minPress

    print(partA)

        


