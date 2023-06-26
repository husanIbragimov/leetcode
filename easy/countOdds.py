# 1523. Count Odd Numbers in an Interval Range


def countOdds(low: int, high: int):
    s = 0
    sum = (high-low)//2
    if low % 2 == 1 or high % 2 == 1:
        s = 1
    else: 
        s = 0
        
    return sum + s

print(countOdds(3, 8))
