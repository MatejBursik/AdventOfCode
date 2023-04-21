cups = 974618352
array = []

for cup in str(cups):
    array.append(int(cup))

cc = 0,array[0]
removed_cups = []

for i in range(3):
    try:
        removed_cups.append(array[cc[0]+1])
        array.pop(cc[0]+1)
    except:
        removed_cups.append(array[0])
        array.pop(0)

i = 1
while True:
    if cc[1]-i in array:
        dc = array.index(cc[1]-i),cc[1]-i
        break
    elif cc[1]-i > 0:
        i+=1
    else:
        cc = array.index(max(array)), max(array)

for i in range(3):
    array.insert(dc[0]+1, removed_cups[len(removed_cups)-1])
    removed_cups.pop(len(removed_cups)-1)

try:
    cc = cc[0]+1, array[cc[0]+1]
except:
    cc = 0, array[0]

print(cc)
print(array)
print(removed_cups)
print(dc)