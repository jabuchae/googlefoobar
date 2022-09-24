def solution(x, y):
    add_x = (x * (x+1)) / 2
    add_y = ((y+x-2) * (y+x-1)) / 2 - (((x-1)*x)/2)

    return str(int(add_x+add_y))


if __name__ == "__main__":
    print(solution(3, 2))
