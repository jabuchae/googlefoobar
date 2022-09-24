class Bombs:
    def __init__(self, m, f):
        self.m = m
        self.f = f

    def grow_ms(self):
        return Bombs(self.m + self.f, self.f)

    def shrink_ms(self, times=1):
        return Bombs(self.m - (self.f*times), self.f)
    
    def grow_fs(self):
        return Bombs(self.m, self.f + self.m)
    
    def shrink_fs(self, times):
        return Bombs(self.m, self.f - (self.m*times))

    def to_string(self):
        return str(self.m) + '-' + str(self.f)

        
def solution(mgoal, fgoal):
    bombs = Bombs(int(mgoal), int(fgoal))
    iters = 0
    while bombs.f > 1 and bombs.m > 1:
        if bombs.f > bombs.m:
            times = int(bombs.f/bombs.m)
            bombs = bombs.shrink_fs(times)
        else:
            times = int(bombs.m/bombs.f)
            bombs = bombs.shrink_ms(times)
        iters += times
    if bombs.m > 1 and bombs.f == 1:
        iters += bombs.m-1
        bombs.m = 1
    if bombs.f > 1 and bombs.m == 1:
        iters += bombs.f-1
        bombs.f = 1
    return str(iters) if bombs.m==1 and bombs.f==1 else "impossible"

def explore_states(s, iters):
    to_process = [s]
    next_up = []
    iteration = 0
    while iteration < iters:

        print(f"Iteration {iteration}") 
        print("") 
        while len(to_process) > 0:
            state = to_process.pop(0)
            print(state.to_string())
            next_up.append(state.grow_ms())
            next_up.append(state.grow_fs())
        
        to_process = next_up
        next_up = []
        iteration += 1

if __name__ == "__main__":
    print(solution(4, 7))
    print(solution(2, 1))

    # explore_states(Bombs(1, 1), 5)