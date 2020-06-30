from modules.classes import UrinalSession, StallRow, Stall
import time


def get_lowest_exposure(occupancy, stalls):
    vacant = [i for j, i in enumerate(stalls) if j not in occupancy]
    if len(occupancy) % 2 == 0:
        vacant.reverse()
    lowest_exposure = sorted(
        vacant, key=lambda stall: stall.exposure, reverse=False
    )[0]
    return lowest_exposure


def print_stalls(st):
    for stall in st:
        icon = 'x' if stall.time > 0 else 'o'
        print(f'|{icon}|', end='')
    print('\r')


def run_cycles(session, stall_row, stalls):
    for cycle in range(session.total_duration):
        interval = cycle % session.cycle_interval == 0

        """
        Check if someone is leaving, update stall occupancy. We do this first
        because want to allow someone to leave a stall and newcomer to enter
        it in same cycle.
        """
        stall_row.update_occupancy(stalls)

        """
        Decrement the time of every occupied stall by one.
        """
        for stall in stalls:
            stall.decrememt_time()

        """
        If occupancy is at maximum, check interval and add to queue if needed.
        """
        stall_row.incrememt_queue(
            interval, stall_row.occupancy, session.stall_count
        )

        """
        Do not continue current loop if there are no vacant stalls.
        """
        if stall_row.queued > 0:
            continue

        """
        The below block of code applies at an interval (someone enters the
        room) or at a cycle when the queue is >0 (someone is already there,
        waiting for a vacant stall).
        """
        if interval or stall_row.queued > 0:
            """
            Stall exposure should be calculated before assigning a stall, as
            if someone left during the same cycle this would affect exposure.
            """
            for stall in stalls:
                stall.set_exposure(session.cycle_duration, stalls)

            """
            Determine which stall has the lowest exposure and assign it to the
            newcomer.
            """
            low_exp_stall = get_lowest_exposure(stall_row.occupancy, stalls)
            low_exp_stall.add_occupant(session.cycle_duration)

            """
            Print stalls to console. This only happens when someone enters a
            stall. Nothing is printed when someone exits a stall.
            """
            print_stalls(stalls)

            """
            Decrement queue if someone in queue and just took a stall.
            """
            stall_row.decrememt_queue()

            """
            Make the console output easier on the eyes before printing next
            change in occupancy.
            """
            time.sleep(1 / 5)

def initialise():
    session = UrinalSession(
        cd=int(input("Enter cycle duration: ")),
        cc=int(input("Enter number of cycles to run: ")),
        ci=int(input("Enter interval between cycles: ")),
        sc=int(input("Enter number of stalls: "))
    )
    stall_row = StallRow()
    stalls = [Stall(stall) for stall in range(session.stall_count)]

    run_cycles(session, stall_row, stalls)

if __name__ == '__main__':
    initialise()
