def calc_last(values):
    if not values or len(list(filter(lambda x: x!=0, values))) == 0: # empty list or all zeros
        return values + [0]

    # calculate the differences between consecutive values
    diff = []
    for i in range(len(values) - 1):
        diff.append(values[i + 1] - values[i])

    # recursively update
    updated = calc_last(diff)
    last = values[-1] + updated[-1]

    return values + [last]

def calc_first(values):
    if not values or len(list(filter(lambda x: x!=0, values))) == 0: # empty list or all zeros
        return [0] + values

    # calculate the differences between consecutive values
    diff = []
    for i in range(len(values) - 1):
        diff.append(values[i + 1] - values[i])

    # recursively update
    updated = calc_first(diff)
    first = values[0] - updated[0]

    return [first] + values

total = []
with open("2023\\09\\input.txt","r") as f:
    for line in f:
        data = list(map(lambda x:int(x), line.strip().split(" ")))
        total.append(calc_last(data)[-1])

print("Part 1:", sum(total))

total = []
with open("2023\\09\\input.txt","r") as f:
    for line in f:
        data = list(map(lambda x:int(x), line.strip().split(" ")))
        total.append(calc_first(data)[0])

print("Part 2:", sum(total))
