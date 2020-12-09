#!/usr/bin/env python

lines = [s.strip() for s in open('input.txt').readlines()]
for a in lines:
    for b in lines:
        for c in lines:
            if int(a) + int(b) + int(c) == 2020:
                print(int(a) * int(b) * int(c))
                exit()
