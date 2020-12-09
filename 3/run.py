rows = [l.strip() for l in open('input.txt').readlines()]


def slide(x_step, y_step):
    tree_count = 0
    x_offset = 0
    for y_offset in range(y_step, len(rows), y_step):
        x_offset = (x_offset + x_step) % len(rows[0])
        # print(rows[y_offset])
        c = rows[y_offset][x_offset]
        # print(y_offset, c)
        if c == '#':
            tree_count += 1

    return tree_count


print(f'rows: {len(rows)}')
print(slide(1, 1))
print(slide(3, 1))
print(slide(5, 1))
print(slide(7, 1))
print(slide(1, 2))
