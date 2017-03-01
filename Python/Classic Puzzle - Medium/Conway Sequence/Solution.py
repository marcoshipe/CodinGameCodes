def conway_sequence_get_next_line(actual_line):
    actual_ch = actual_line[0]
    amount = 0
    next_line = []
    for ch in actual_line:
        if ch != actual_ch:
            next_line.append(amount)
            next_line.append(actual_ch)
            actual_ch = ch
            amount = 1
        else:
            amount += 1
    next_line.append(amount)
    next_line.append(actual_ch)
    return next_line

r = int(input())  # The original number R of the sequence.
l = int(input())  # The line L to display. The index of the first line is 1.

list = [r]
for _ in range(l-1):
    list = conway_sequence_get_next_line(list)
print(" ".join(str(x) for x in list))
