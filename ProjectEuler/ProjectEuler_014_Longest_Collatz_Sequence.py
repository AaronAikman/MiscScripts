from ProjectEulerUtils import find_collatz_sequence

x = 999999
# collatz_starts = []
collatz_lengths = []
collatz_dict = {}
while x > 1:
    collatz_dict[str(len(find_collatz_sequence(x)))] = x
    # collatz_starts.append(x)
    print x, 'goes for', len(find_collatz_sequence(x))
    # collatz_lengths.append(len(find_collatz_sequence(x)))
    x -= 1
# m = max(collatz_lengths)
collatz_lengths = map(int, collatz_dict.keys())
m = max(collatz_lengths)
print 'max =', m
# which = [k for k, v in enumerate(collatz_lengths) if v == m]
# print collatz_lengths[which[0]], '= which num'
print 'the starting number =', collatz_dict[str(m)]