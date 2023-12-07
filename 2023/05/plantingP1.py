"""
seed_to_soil map:
50 98 2
52 50 48

seed number (the source) to a soil number (the destination)
destination range start ; source range start ; range length

source numbers that aren't mapped correspond to the same destination number

? What is the lowest location number that corresponds to any of the initial seed numbers
"""

class instruction():
    def __init__(self,destination,source,range):
        self.destination = int(destination)
        self.source = int(source)
        self.range = int(range)

# sd = int 
def testing(inst,sd):
    for obj in inst:
        if sd >= obj.source and sd < obj.source + obj.range -1:
            diff = sd - obj.source
            sd = obj.destination + diff
            return sd
    return sd

# reading the file and preparing the intructions
with open("2023\\05\\input.txt", "r") as f:
    seeds = list(map(lambda x:int(x), f.readline().strip().split(": ")[1].split(" ")))
    
    f.readline()
    data = f.readline()

    seed_to_soil = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        seed_to_soil.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    soil_to_fertilizer = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        soil_to_fertilizer.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    fertilizer_to_water = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        fertilizer_to_water.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    water_to_light = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        water_to_light.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    light_to_temperature = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        light_to_temperature.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    temperature_to_humidity = []
    while data != "\n":
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        temperature_to_humidity.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

    data = f.readline()

    humidity_to_location = []
    while data != "\n" and data:
        if ":" in data:
            data = f.readline()
            continue
        data = list(map(lambda x:int(x),data.strip().split(" ")))
        humidity_to_location.append(instruction(data[0],data[1],data[2]))
        data = f.readline()

locations = []
for seed in seeds:
    seed = testing(seed_to_soil,seed)
    seed = testing(soil_to_fertilizer,seed)
    seed = testing(fertilizer_to_water,seed)
    seed = testing(water_to_light,seed)
    seed = testing(light_to_temperature,seed)
    seed = testing(temperature_to_humidity,seed)
    seed = testing(humidity_to_location,seed)

    locations.append(seed)

print("Part 1, lowest location number:", min(locations))
