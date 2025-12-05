
with open("inputTxt.txt", "r") as f:
    lines = f.readlines()

    freshes = []
    isFreshInputs=True
    availables = []
    i = 0
    for line in lines:
        line = line.strip()

        if not line:
            isFreshInputs = False
            freshes.sort()
            i = 0
            continue

        if isFreshInputs:
            low, high = line.split("-")
            low = int(low)
            high = int(high)

            freshes.append([low, high])

            
        else:
            item = int(line)
            availables.append(item)
    
    availables.sort()

    # print(freshes)
    usable = 0


    for available in availables:
        low, high = freshes[i]

        # print(available, freshes[i])

        used = False
        
        while i < len(freshes) and high < available:
            low, high = freshes[i]
            i += 1
            used = True
        
        if used:
            i -= 1
        
        # print(i)

        if available <= high and available >= low:
            usable += 1

        


    print(usable)
