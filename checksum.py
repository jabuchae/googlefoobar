from functools import reduce


def getRow(start, length):
    if length == 0:
        return 0
    
    if length == 1:
        return start

    if start % 2 == 1:
        return start ^ getRow(start+1, length -1)

    nums = [0, start+length-1, 1, start+length]
    return nums[length % 4]

def solution(start, length):
    nums = list(range(0, length))
    rows = map(lambda x: getRow(start+length*x, length-x), nums)
    return reduce(lambda x, y: x ^ y, rows, 0)
