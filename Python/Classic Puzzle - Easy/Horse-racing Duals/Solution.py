n = int(input())  # number of horses
horses_strengths = []  # [horse_strength_1, horse_strength_2, ...]
for i in range(n):
    horses_strengths.append(int(input()))

horses_strengths.sort()
min_dist = abs(horses_strengths[0] - horses_strengths[1])
for i in range(1, len(horses_strengths)):
    act_dist = abs(horses_strengths[i] - horses_strengths[i - 1])
    if act_dist < min_dist:
        min_dist = act_dist

print(str(min_dist))
