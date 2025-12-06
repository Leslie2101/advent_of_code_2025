
print("----------- PART A ---------------")

# Part A
with open("inputTxt.txt", "r") as f:
    lines = f.readlines()

    lines = [line.strip().split() for line in lines]
    
    cols = len(lines[0])

    ops = lines[-1]


    functionMap = {
        "*": lambda x, y: x*y,
        "+": lambda x, y: x+y
    }

    cur = [int(ch) for ch in lines[0]]

    for line in lines[1:-1]:
        line = [int(x) for x in line]
        for i in range(cols):

            cur[i] = functionMap[ops[i]](cur[i], line[i])
    

    print(sum(cur))




print("-------------PART B--------------")



# Part B

with open("inputTxt.txt", "r") as f:
    lines = f.readlines()
    cols = len(lines[0].split())

    ops = lines[-1]


    indices = []
    start = -1

    for i in range(len(ops)):
        if ops[i] != " ":
            if start != -1:
                indices.append((start, i))
            start = i
    

    indices.append((start, max([len(line) for line in lines])))

        

    functionMap = {
        "*": lambda x, y: x*y,
        "+": lambda x, y: x+y
    }


    def helper(prev, cur):
        maxLength = max(len(prev), len(cur))

        minLength = min(len(prev), len(cur))

        res = [0] * maxLength
        for i in range(0, minLength):
            res[i] = prev[i] + cur[i]
        
        

        maxArr = prev if len(prev) > len(cur) else cur

        for i in range(minLength, maxLength):
            res[i] = maxArr[i]
        
        return res

    def splitByIndices(line, indices):
        res = [line[i:j-1] for i, j in indices]
        return res
            


    cur =  splitByIndices(lines[0], indices)

    for line in lines[1:-1]:
        line = splitByIndices(line, indices)
        for i in range(cols):
            cur[i] = helper(cur[i], line[i])
    

    ops = ops.split()

    res = 0
    for i in range(cols):
        colNums = cur[i]

        
        val = int(colNums[0])
        for num in colNums[1:]:
            
            print(val, end="")
            val = functionMap[ops[i]](val, int(num))

            print(f" {ops[i]} {num} = {val}")

        res += val

        print("-----------")

      
    print(res)