

def partA():
    with open("inputTxt.txt", "r") as f:
        lines = f.readlines()


        beams = set()
        cnt = 0
        for line in lines:
            line = line.strip()

            for i in range(len(line)):
                ch = line[i]

                if ch == "S":
                    beams.add(i)
                
                    continue
                    
                if ch == "^" and i in beams:
                    beams.remove(i)
                    cnt += 1
                    
                    if i-1 >= 0:
                        beams.add(i-1)
                    
                    if i+1 < len(line):
                        beams.add(i+1)
                


        print(cnt)



def partB():
    with open("inputTxt.txt", "r") as f:
        lines = f.readlines()


        beams = set()
        cnt = 0

        n = len(lines[0])
        prev = [1] * n



        for line in lines[::-1]:
            line = line.strip()
            cur = [0] * n

            for i in range(len(line)):
                ch = line[i]

                if ch == ".":
                    cur[i] = prev[i]

                elif ch == "^":

                    if i-1 >= 0:
                        cur[i] += prev[i-1]
                    
                    if i+1 < n:
                        cur[i] += prev[i+1]
                    
                elif ch == "S":
                    cur[i] = prev[i]
                    print(cur[i])
                    return 
                else:
                    print("unknown: ", line[i]) 
                        
            prev = cur
            

                


print(partB())

                


