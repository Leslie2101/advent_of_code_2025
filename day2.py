inputs = ""


ranges = input().split(",")


def isValid(num: int):
    num_str = str(num)


    for i in range(1, len(num_str)//2 + 1):
        prefix = num_str[:i]

        if len(num_str) % len(prefix) != 0:
            continue

        repeat_cnt = len(num_str) // len(prefix)

        if prefix * repeat_cnt == num_str:
            return True
    
    return False



total = 0

for range_str in ranges:
    lower, higher = range_str.split("-")
    lower= int(lower)
    higher = int(higher)
    for num in range(lower, higher + 1):
        if isValid(num):
            total += num

print(total)

