#!/usr/bin/env python
import re
from collections import namedtuple

Row = namedtuple('Row', 'l h c s')
rgx = re.compile('(\\d+)-(\\d+) (\\w): (\\w+)')


def parse_row(s):
    l, h, c, s = rgx.match(s.strip()).groups()
    return Row(l=int(l), h=int(h), c=c, s=s)


def c1(row):
    return row.l <= ct <= row.h


def c2(row):
    matches = (row.s[row.l-1] == row.c) + (row.s[row.h-1] == row.c)
    return matches == 1


c_fn = c2

valid = 0

rows = [parse_row(s) for s in open('input.txt').readlines()]
for row in rows:
    ct = 0
    for c in row.s:
        if row.c == c:
            ct += 1

    if c_fn(row):
        valid += 1

print(valid)
