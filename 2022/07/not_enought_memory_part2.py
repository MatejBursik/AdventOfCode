class Dir:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.size_below = size


with open("AdventOfCode\\2022\\07\\input.txt") as f:
    data = f.readlines()
    arr = [i.replace("\n", "").split(" ") for i in data]

#tree making
root = Dir(0)
index = 1
dir_dict = {}
curr = root
for line in arr:
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

#getting total size
total_used = root.size_below
total_free = 70000000 - total_used
amount_to_delete = 30000000 - total_free

#finding the smallest directory to delete
answer = root.size_below
for index, dir in dir_dict.items():
    if (len(dir.contents) > 0) and (dir.size_below < answer) and (dir.size_below >= amount_to_delete):
        answer = dir.size_below

print(answer)
