import sys
import os
from lab5.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class NetworkPacketsProcessor:
    def __init__(self):
        input_file = read_input(task=3)
        first_line = input_file[0].split()
        self.buffer_size = int(first_line[0])
        self.n = int(first_line[1])
        self.packets = [list(map(int, i.split())) for i in input_file[1:] if len(i.split()) == 2]
        self.buffer = []
        self.start_times = []

    def network_packets(self, buffer_size, packets, n):
        for packet in packets:
            if len(packet) != 2:
                print(f"Неверный пакет: {packet}")
                continue

            arrival_time, processing_time = packet

            while self.buffer and self.buffer[0] <= arrival_time:
                self.buffer.pop(0)

            if len(self.buffer) >= self.buffer_size:
                self.start_times.append('-1')
            else:
                start_time = arrival_time if not self.buffer else self.buffer[-1]
                self.start_times.append(str(start_time))
                self.buffer.append(start_time + processing_time)

        return self.start_times


def main():
    npp = NetworkPacketsProcessor()
    res = npp.network_packets(npp.buffer_size, npp.packets, npp.n)
    write_output(3, *res)


if __name__ == "__main__":
    decorate(task=3, task_name='network_packet')
