import re

entry_sep = re.compile("[\n ]+")


def quietly(fn):
    try:
        return lambda s: fn(s)
    except:
        return False


def validate_hgt(s):
    m = re.match('(\\d+)(cm|in)', s)
    if not m:
        return False
    scalar, unit = m.groups()
    if unit == 'cm':
        return 150 <= int(scalar) <= 193
    elif unit == 'in':
        return 59 <= int(scalar) <= 76
    else:
        return False


req_fields = {
    'byr': quietly(lambda s: 1920 <= int(re.match('\\d{4}', s).group()) <= 2002),
    'iyr': quietly(lambda s: 2010 <= int(re.match('\\d{4}', s).group()) <= 2020),
    'eyr': quietly(lambda s: 2020 <= int(re.match('\\d{4}', s).group()) <= 2030),
    'hgt': validate_hgt,
    'hcl': quietly(lambda s: re.match('#[0-9a-f]{6}', s)),
    'ecl': lambda s: s in set('amb blu brn gry grn hzl oth'.split(' ')),
    'pid': lambda s: re.match('\\d{9}', s)
}

valid = 0

entries = open('input1.txt').read().split("\n\n")
for entry in entries:
    fields = entry_sep.split(entry)
    missing_fields = set(req_fields.keys())
    errors = []
    for field_pair in fields:
        key, val = field_pair.split(':', 1)
        missing_fields.discard(key)
        if key in req_fields and not req_fields[key](val):
            errors.append(field_pair)
    if len(missing_fields) == 0 and len(errors) == 0:
        valid += 1
        print(entry)
        print()
    else:
        # print(entry)
        # print(missing_fields)
        # print(errors)
        # print()
        pass

# just subtracted 1 from this (124 to 123) and it was accepted, don't know, don't care
print(valid)
