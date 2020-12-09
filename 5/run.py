import pydash

ROW = 0
COL = 1
ID = 2


def parse_line(s):
    bits = s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    row = int(str(bits[:7]), 2)
    col = int(str(bits[7:]), 2)
    return row, col, row * 8 + col


passes = [parse_line(l.strip()) for l in open('input.txt').readlines()]

print(pydash.max_by(passes, ID))

spasses = pydash.sort_by(passes, ID)
for idx in range(0, len(spasses) - 1):
    if spasses[idx][ID] == spasses[idx + 1][ID] - 2:
        print(spasses[idx][ID] + 1)
        break
