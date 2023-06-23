with open('input.txt') as fp:
    lines = fp.readlines()
    distance = int(lines[0])
    tank_size = int(lines[1])
    gas_stations = lines[3]

gas_stations_count = len(gas_stations.split())
gas_stations = [int(i) for i in gas_stations.split()]

def car_fueling(distance, tank_size, gas_stations_count, gas_stations):
    num_refill, curr_refill, limit = 0, 0, tank_size
    while limit < distance:
        if curr_refill >= gas_stations_count or gas_stations[curr_refill] > limit:
            return -1
        while curr_refill < gas_stations_count-1 and gas_stations[curr_refill + 1] <= limit:
            curr_refill += 1
        num_refill += 1
        limit = gas_stations[curr_refill] + tank_size
        curr_refill += 1
    return num_refill

f = open('output.txt', 'w')
f.write(str(car_fueling(distance, tank_size, gas_stations_count, gas_stations)))
