def find_overlap(r1, r2):
    """takes two ranges as input ; returns the overlapping portion of the two ranges"""
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    o_start = max(r1_start, r2_start)
    o_end = min(r1_end, r2_end)

    if o_start <= o_end:
        return (o_start, o_end)
    
    return  False

def split_range(r, overlap):
    """takes a range and an overlaping range ; returns a set of non-overlapping ranges"""
    result = set()
    o_start, o_end = overlap
    r_start, r_end = r

    if r_start < o_start:
        result.add((r_start, o_start-1))
    if r_end > o_end:
        result.add((o_end+1, r_end))

    return result

mapData = []
with open("2023\\05\\input.txt", "r") as f:
    seeds = list(map(lambda x:int(x), f.readline().strip().split(": ")[1].split(" ")))
    for line in f:
        if line != '\n':
            mapData[-1].append(line.strip())
        else:
            mapData.append([])

maps = []
for mp in mapData:
    hold = []
    for ins in mp[1:]:
        hold.append(list(map(lambda x:int(x), ins.split(" "))))
    maps.append(hold)

ranges = set(map(lambda s_c: (s_c[0], s_c[0] + s_c[1] -1), zip(seeds[0::2], seeds[1::2])))

for mp in maps:
    shifted_ranges = set()
    for dest, source, m_range in mp:
        for r in ranges.copy():
            if overlap := find_overlap(r, (source, source + m_range -1)):
                ranges.remove(r)
                ranges.update(split_range(r, overlap))
                shifted_ranges.add((overlap[0] + dest - source, overlap[1] + dest - source))

    ranges.update(shifted_ranges)

print("Part 2, lowest location number:", min(min(ranges)))
