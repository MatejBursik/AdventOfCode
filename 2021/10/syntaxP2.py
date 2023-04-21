lines = []

with open("AdventOfCode\\2021\\10\\input.txt","r") as f:
    for l in f:
        lines.append(l.strip("\n"))

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

bracket_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

total_scores = []

for line in lines:
    is_corrupt = False
    stack = []
    for char in line:
        arr = char == '>' and len(stack) > 0 and stack[-1] == '<'
        squar = char == ']' and len(stack) > 0 and stack[-1] == '['
        snake = char == '}' and len(stack) > 0 and stack[-1] == '{'
        Brk = char == ')' and len(stack) > 0 and stack[-1] == '('
        if arr or squar or snake or Brk:
            stack.pop()
        elif char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            # Break, and ignore the corrupt lines
            is_corrupt = True
            break

    if is_corrupt:
        continue
    score = 0
    stack.reverse()

    for char in stack:
        score = score * 5 + points[bracket_mapping[char]]
    total_scores.append(score)
    
total_scores.sort()
print("Total scores: " + str(f'{total_scores[len(total_scores) // 2]}'))