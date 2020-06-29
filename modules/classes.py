class UrinalSession:
    def __init__(self, cd, cc, ci, sc):
        self.cycle_duration = cd
        self.cycle_count = cc
        self.cycle_interval = ci
        self.stall_count = sc
        self.total_duration = cd * cc


class StallRow:
    def __init__(self):
        self.queued = 0
        self.occupancy = []

    def update_occupancy(self, stalls):
        occupied = []
        for i, stall in enumerate(stalls):
            if int(stall.time) > 0:
                occupied.append(i)
        self.occupancy = occupied

    def incrememt_queue(self, interval, occupancy, stall_count):
        if interval and len(occupancy) >= stall_count:
            self.queued += 1

    def decrememt_queue(self):
        if self.queued > 0:
            self.queued -= 1


class Stall:
    def __init__(self, position):
        self.position = position
        self.exposure = 0
        self.time = 0

    def set_exposure(self, duration, stalls):
        i = self.position
        exposure = 0
        if i > 0:
            exposure += stalls[i-1].time * (100 / duration)
        if i+1 <= len(stalls)-1:
            exposure += stalls[i+1].time * (100 / duration)
        self.exposure = exposure

    def decrememt_time(self):
        time = int(self.time)
        if time > 0:
            self.time = time - 1

    def add_occupant(self, duration):
        if self.time == 0:
            self.time = duration
        else:
            print('Error: add_occupant() attmped to populate non-vacant stall')
            raise
