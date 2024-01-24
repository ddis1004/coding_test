N, S, M = map(int, input().split())
V = list(map(int, input().split()))

max_volume = -1
stage_memory = [[] for i in range(N+1)]

def start_stage(s):
    v = V[s]
    if len(stage_memory[s]) == 0: #it's just not possible
        return False
    #print(f'possible current volume at this time is {stage_memory[s]}')
    for current_vol in stage_memory[s]:
        #print(f' current_vol + v : {current_vol + v} current_vol - v : {current_vol - v}')
        if current_vol + v <= M and not current_vol + v in stage_memory[s+1]:
            stage_memory[s + 1].append(current_vol + v)
        if current_vol - v >= 0 and not current_vol - v in stage_memory[s+1]:
            stage_memory[s + 1].append(current_vol - v)
    return True

stage_memory[0].append(S)


def run_through_stage(N):
    for i in range(N):
        result = start_stage(i)
        if not result:
            return False
    return True

if run_through_stage(N) == True:
    if len(stage_memory[N]) > 0:
        print(max(stage_memory[N]))
    else:
        print(-1)
else:
    print(-1)
