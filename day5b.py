
def help():
    with open("inputTxt.txt", "r") as f:
        lines = f.readlines()
        intervals = []
        for line in lines:
            line = line.strip() 
            
            if not line:
                break 
            
            low, high = [int(x) for x in line.split("-")]
            intervals.append([low, high])

        intervals.sort()

        # split into non-overlapping intervals here
        new_intervals = []

        low, high = intervals[0]
        cnt = 0
        for i in range(1, len(intervals)):
            left, right = intervals[i]

            if left <= high:
                # merge to previous interval
                high = max(high, right)
            else:
                cnt += (high - low + 1)

                # new interval begins
                low, high = left, right 
        
        # add final intervals 
        cnt += (high - low + 1)

        return cnt
    
print(help())
        
            

