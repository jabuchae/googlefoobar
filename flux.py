parents = {}

def getParent(num, root, min):
    middle = int((root + min) / 2)
    right = root-1
    left = middle-1
    
    if num == right or num == left:
        return root

    if num < middle:
        return getParent(num, left, min)
    else:
        return getParent(num, right, left+1)

def solution(h, l):
    root = pow(2, h) -1

    ret = []
    for num in l:

        if num == root:
            ret.append(-1)
        else:    
            ret.append(getParent(num, root, 1))

    return ret


if __name__ == "__main__":
    for item in solution(3, [1, 2, 3, 4, 5, 6, 7]):
        print(item)