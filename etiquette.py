from modules.classes import UrinalSession, StallRow, Stall
import time


def run_cycles(session, stall_row, stalls):
    for cycle in range(session.total_duration):
        stall_row.occupancy = get_occupied_stalls(stalls)

        if len(stall_row.occupancy) >= session.stall_count:
            if cycle % session.cycle_interval == 0:
                stall_row.queued += 1
            continue

        if cycle % session.cycle_interval == 0 or stall_row.queued > 0:
            process_cycle(stall_row.occupancy, session.cycle_duration, stalls)
            if stall_row.queued > 0:
                stall_row.queued -= 1
            time.sleep(1/5)


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
        lowest_exposure = sorted(
            vacant, key=lambda stall: stall.exposure, reverse=False
        )[0]
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


if __name__ == '__main__':
    session_obj = UrinalSession()
    stall_row_obj = StallRow()
    stalls_obj = [Stall(stall) for stall in range(session_obj.stall_count)]
    run_cycles(session_obj, stall_row_obj, stalls_obj)
