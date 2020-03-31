import time

class Stall():
    def __init__(self,stall):
        self.position = stall
        self.exposure = 0
        self.time = 0

    def __str__(self):
        return f"[{self.position}] exposure: {self.exposure}, time: {self.time}"

    def set_exposure(self):
        def threat(neighbour):
            return neighbour.time * (100 / cycle_duration)

        i = self.position
        exposure = 0
        if i > 0:
            exposure += threat(stalls[i-1])
        if i+1 <= len(stalls)-1:
            exposure += threat(stalls[i+1])
        self.exposure = exposure

    def set_time(self):
        time = int(self.time)
        if time > 0:
            self.time = time - 1
        return self.time

def get_occupancy():
    occupied = []
    for i, stall in enumerate(stalls):
        time = int(stall.set_time())
        if time > 0:
            occupied.append(i)
    return occupied

def process_cycle(occupied):
    def add_occupant(occupied):
        vacant = [i for j, i in enumerate(stalls) if j not in occupied]
        if len(occupied) % 2 == 0:
            vacant.reverse()
        lowest_exposure = sorted(vacant, key=lambda stall: stall.exposure, reverse=False)[0]
        lowest_exposure.time = cycle_duration

    def process_stalls():
        for stall in stalls:
            stall.set_exposure()

    def print_stalls():
        for stall in stalls:
            icon = 'x' if stall.time > 0 else 'o'
            print(f'|{icon}|', end='')
        print('\r')

    add_occupant(occupied)
    process_stalls()
    print_stalls()

cycle_duration = int(input("Enter cycle duration: ")) #20
cycle_count = int(input("Enter number of cycles to run: ")) #10
cycle_interval = int(input("Enter interval between cycles: ")) #3
stall_count = int(input("Enter number of stalls: ")) #10

total_duration = cycle_duration * cycle_count + 1
queued = 0
stalls = [Stall(stall) for stall in range(stall_count)]

for cycle in range(total_duration):
    occupied = get_occupancy()

    if len(occupied) >= stall_count:
        if cycle%cycle_interval == 0:
            queued += 1
        continue

    if cycle%cycle_interval == 0 or queued > 0:
        process_cycle(occupied)
        if queued > 0:
            queued -= 1
        time.sleep(1/5)
