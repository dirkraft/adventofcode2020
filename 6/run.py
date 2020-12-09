import re

groups = re.split('\n\n', open('input.txt').read())

sum = 0

for group in groups:
    peeps = group.split('\n')
    answer_cts = {}
    for p in peeps:
        for answer in p:
            if answer not in answer_cts:
                answer_cts[answer] = 0
            answer_cts[answer] += 1
    for ct in answer_cts.values():
        if ct == len(peeps):
            sum += 1

print(sum)
