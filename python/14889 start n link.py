N = int(input())
S = []

for i in range(N):
    S.append(list(map(int, input().split())))

# stack = [(team1, team2, score1, score2)]
stack = [(set([0]), set(), 0, 0)]  # 0부터 시작하는 팀, set 사용

answer = float('inf')

def score_add(team, new_member):
    score_sum = 0
    for i in team:
        score_sum += S[i][new_member] + S[new_member][i]
    return score_sum

while stack:
    team1, team2, score1, score2 = stack.pop()
    depth = len(team1) + len(team2)

    if depth == N:
        answer = min(abs(score1 - score2), answer)
        continue

    # team1의 복사본을 사용하여 새로운 상태 추가 (set 사용)
    if len(team1) < N // 2:
        add_score = score_add(team1, depth)
        new_team1 = team1 | {depth}  # set에 새 원소 추가
        stack.append((new_team1, team2.copy(), score1 + add_score, score2))

    # team2의 복사본을 사용하여 새로운 상태 추가 (set 사용)
    if len(team2) < N // 2:
        add_score = score_add(team2, depth)
        new_team2 = team2 | {depth}  # set에 새 원소 추가
        stack.append((team1.copy(), new_team2, score1, score2 + add_score))

print(answer)