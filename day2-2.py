"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

passblob = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

with open('input_day2') as f:
    passblob = f.read()

passlist = passblob.split('\n')

valid_count = 0

for line in passlist:
    kv = line.split(': ')
    if len(kv) != 2:
        continue
    pw = list(kv[1])
    rule = kv[0].split(' ')
    if len(rule) != 2:
        continue
    char = rule[1]
    pos = rule[0].split('-')
    if len(pos) != 2:
        continue
    
    first = int(pos[0]) - 1
    second = int(pos[1]) - 1
    if (pw[first] == char) ^ (pw[second] == char): # XOR
        valid_count += 1

print(valid_count)
