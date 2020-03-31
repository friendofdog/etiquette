from modules.classes import StallRow, Stall
import time


def get_occupied_stalls(stalls):
    occupied = []
    for i, stall in enumerate(stalls):
        if int(stall.set_time()) > 0:
            occupied.append(i)
    return occupied


def process_cycle(occupied, cycle_duration, stalls):
    def add_occupant():
        vacant = [i for j, i in enumerate(stalls) if j not in occupied]
        if len(occupied) % 2 == 0:
            vacant.reverse()
        lowest_exposure = sorted(vacant, key=lambda stall: stall.exposure, reverse=False)[0]
        lowest_exposure.time = cycle_duration

    def process_stalls():
        for stall in stalls:
            stall.set_exposure(cycle_duration, stalls)

    def print_stalls():
        for stall in stalls:
            icon = 'x' if stall.time > 0 else 'o'
            print(f'|{icon}|', end='')
        print('\r')

    add_occupant()
    process_stalls()
    print_stalls()


def run_script():
    cycle_duration = int(input("Enter cycle duration: "))  # 20
    cycle_count = int(input("Enter number of cycles to run: "))  # 10
    cycle_interval = int(input("Enter interval between cycles: "))  # 3
    stall_count = int(input("Enter number of stalls: "))  # 10
    total_duration = cycle_duration * cycle_count + 1

    stall_row = StallRow()
    stalls = [Stall(stall) for stall in range(stall_count)]

    for cycle in range(total_duration):
        stall_row.occupancy = get_occupied_stalls(stalls)

        if len(stall_row.occupancy) >= stall_count:
            if cycle%cycle_interval == 0:
                stall_row.queued += 1
            continue

        if cycle%cycle_interval == 0 or stall_row.queued > 0:
            process_cycle(stall_row.occupancy, cycle_duration, stalls)
            if stall_row.queued > 0:
                stall_row.queued -= 1
            time.sleep(1/5)


if __name__ == '__main__':
    run_script()