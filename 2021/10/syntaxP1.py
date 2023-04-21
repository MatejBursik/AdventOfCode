lines = []

with open("AdventOfCode\\2021\\10\\input.txt","r") as f:
    for l in f:
        lines.append(l.strip("\n"))

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

illegal_chars = []

for line in lines:
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
            # Collect all illegal chars
            illegal_chars.append(char)
            break
print("Total illegal points: " + str(f'{sum([illegal_points[char] for char in illegal_chars])}'))