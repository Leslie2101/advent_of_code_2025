



def getNeighbors(x: int, y: int, rows: int, cols: int):
    res = []

    diffs = [-1, 0, 1]

    for xDiff in diffs:
        for yDiff in diffs:
            if xDiff == 0 and yDiff == 0:
                continue

            newX = x + xDiff
            newY = y + yDiff

            if newX < rows and newX >= 0 and newY < cols and newY >= 0:
                res.append((newX, newY))
    return res



def removeRolls(lines):

    removed = set()
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == ROLL:
                neighbors = getNeighbors(i, j, len(lines), len(lines[i]))

                cnt = 0
                for coord in neighbors:
                    x,y = coord
                    if lines[x][y] == ROLL:
                        cnt += 1
                
                if cnt < 4:
                    total += 1
                    removed.add((i,j))
    return removed, total
    

ROLL = '@'
with open("inputTxt.txt", "r") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    total = 0

    removed, added = removeRolls(lines)

    while added > 0:
        total += added
        for coord in removed:
            x,y = coord
            lines[x][y] = '.'
        
        removed, added = removeRolls(lines)
    
    print(total)
                

            

