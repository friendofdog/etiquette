import time

cycle_duration = int(input("Enter cycle duration: ")) #20
cycle_count = int(input("Enter number of cycles to run: ")) #10
cycle_interval = int(input("Enter interval between cycles: ")) #3
stall_count = int(input("Enter number of stalls: ")) #3
stalls = [{'threat': 0, 'exposure': 0, 'time': 0} for stall in range(stall_count)]
total_duration = cycle_duration * cycle_count + 1
queued = 0

def print_stalls():
    for stall in stalls:
        icon = 'x' if stall['time'] > 0 else 'o'
        print(f'|{icon}|', end = '')

    print('\r')

def find_occupied():
    occupied = []
    for i, stall in enumerate(stalls):
        if stall['time'] > 0:
            occupied.append(i)
    return occupied

def set_threat():
    for stall in stalls:
        stall['threat'] = stall['time'] * (100/cycle_duration)

def set_exposure():
    for i, stall in enumerate(stalls):
        exposure = 0
        if i > 0: exposure += stalls[i-1]['threat']
        if i+1 <= len(stalls)-1: exposure += stalls[i+1]['threat']
        stall['exposure'] = exposure

def add_occupant():
    def assess_exposure():
        exclude = find_occupied()
        vacant = [i for j, i in enumerate(stalls) if j not in exclude]
        if len(exclude) % 2 == 0:
            vacant.reverse()
        return sorted(vacant, key=lambda k: k['exposure'], reverse=False)[0]
    lowest_exposure = assess_exposure()
    lowest_exposure['time'] = cycle_duration

def set_time():
    for i, stall in enumerate(stalls):
        time = int(stall['time'])
        stall['time'] = time-1 if time > 0 else 0

def process_cycle():
    add_occupant()
    set_threat()
    set_exposure()
    print_stalls()

for cycle in range(total_duration):
    set_time()
    occupied = len(find_occupied())
    proceed = False

    if occupied >= stall_count:
        proceed = False
        if cycle%cycle_interval == 0:
            queued += 1
        continue

    if cycle%cycle_interval == 0 or queued > 0:
        process_cycle()
        if queued > 0:
            queued -= 1
        time.sleep(1/5)
