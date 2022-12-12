#!/usr/bin/python3
import sys
import copy

f = sys.argv[1] if len(sys.argv) > 1 else "5.in"
data = open(f).read()
_, instructions = data.strip().split('\n\n')

stacks1 = [
        ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
        ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
        ['C', 'V', 'S', 'H'],
        ['H', 'F', 'G'],
        ['P', 'G', 'J', 'B', 'Z'],
        ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
        ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
        ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
        ['W', 'P', 'V', 'M', 'B', 'H']
        ]

stacks2 = copy.deepcopy(stacks1)


for inst in instructions.split('\n'):
    parts = inst.split(' ')
    k, a, b = int(parts[1]), int(parts[3]), int(parts[5])
    for _ in range(k):
        stacks1[b-1].append(stacks1[a-1].pop())
    stacks2[b-1].extend(stacks2[a-1][-k:])
    stacks2[a-1] = stacks2[a-1][:-k]

order1 = ""
order2 = ""
for stack in stacks1:
    order1 += stack[-1]
for stack in stacks2:
    order2 += stack[-1]

print(order1)
print(order2)
