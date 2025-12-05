


def findMaxJoltage(string: str):
    dp = [None] * 13 

    dp[0] = 0

    res = 0


    for ch in string:
        newDp = [None] * 13
        newDp[0] = 0

        i = 0
        while i < len(dp) - 1 and dp[i] != None:
            val = dp[i]*10 + int(ch)

            if dp[i+1] == None:
                newDp[i+1] = val
            else:
                newDp[i+1] = max(dp[i+1], val)
            
            i+= 1
            

        if newDp[12] != None:
            res = max(res, newDp[12])
        

        dp = newDp

    
    return res



lines = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


with open("inputTxt.txt", "r") as f:
    lines = f.readlines()


lines = [line.strip() for line in lines]

total = 0

for line in lines:
    val = findMaxJoltage(line)
    total += val
    print(val)

print("total: ", total)
        

