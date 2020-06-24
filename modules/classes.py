class UrinalSession:
    def __init__(self):
        self.cycle_duration = int(input("Enter cycle duration: "))
        self.cycle_count = int(input("Enter number of cycles to run: "))
        self.cycle_interval = int(input("Enter interval between cycles: "))
        self.stall_count = int(input("Enter number of stalls: "))
        self.total_duration = self.cycle_duration * self.cycle_count + 1


class StallRow:
    def __init__(self):
        self.queued = 0
        self.occupancy = []


class Stall:
    def __init__(self, stall):
        self.position = stall
        self.exposure = 0
        self.time = 0

    def __str__(self):
        return \
            f"[{self.position}] exposure: {self.exposure}, time: {self.time}"

    def set_exposure(self, cycle_duration, stalls):
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
