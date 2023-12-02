from collections import deque

def mix(data):
    for origin_idx in range(len(data)):
        while data[0][0] != origin_idx:
            data.rotate(-1)
    
        current = data.popleft()
        shift = current[1] % len(data) # value to shift by
        data.rotate(-shift)
        data.append(current)
        
    return data

def coordValue(values, coord):
    idx = (values.index(0) + coord) % len(values)
    return values[idx]

with open("2022\\20\\py\\input.txt", "r") as f:
    data = list(map(int, f.read().splitlines()))

# part 1
data_1 = deque(list(enumerate(data.copy())))
data_1 = mix(data_1)

# part 2
decryption_key = 811589153
decrypted = [val*decryption_key for val in data]
data_2 = deque(list(enumerate(decrypted)))
mixes = 10
for _ in range(mixes):
    data_2 = mix(data_2)

# find coordinates 1000, 2000, 3000th after 0
sum1 = 0
sum2 = 0
for coord in (1000, 2000, 3000):
    sum1 += coordValue([val[1] for val in data_1], coord)
    sum2 += coordValue([val[1] for val in data_2], coord)
    
print("Part 1:",sum1)
print("Part 2:",sum2)
