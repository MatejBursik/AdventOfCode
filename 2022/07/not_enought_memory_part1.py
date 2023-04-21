class Dir:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.size_below = size


with open("AdventOfCode\\2022\\07\\input.txt") as f:
    data = []
    for line in f:
        data.append(line.strip().split(" "))

#tree making
root = Dir(0)
index = 1
dir_dict = {}
curr = root
for line in data:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                directory_name = line[2]
                if directory_name == "/":
                    curr = root
                else:
                    curr = curr.contents[directory_name]
    else:
        if line[0] == "dir":
            directory_name = line[1]
            dir_dict[index] = Dir(index, parent=curr)
            curr.contents[directory_name] = dir_dict[index]
            index += 1
        else:
            size = int(line[0])
            file_name = line[1]
            dir_dict[index] = Dir(index, parent=curr, size=size)
            curr.contents[file_name] = dir_dict[index]
            index += 1

#separating visited and not visited
answer = 0
to_visit = [root]
visited = set()
while len(to_visit) > 0:
    dir = to_visit[-1]
    for sub in dir.contents.values():
        if sub.index not in visited:
            to_visit.append(sub)
            break
    else:
        dir = to_visit.pop()
        visited.add(dir.index)
        if dir.parent is not None:
            dir.parent.size_below += dir.size_below

        #identifying if their size is smaller or equal to 100000
        if (dir.size_below <= 100000) and (len(dir.contents) > 0):
            answer += dir.size_below

print(answer)
