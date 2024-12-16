import unittest

from lab5.task3.src.network_packet import *
from lab5.utils import read_input, write_output, decorate

class TestNetworkPacketsProcessor(unittest.TestCase):
    def setUp(self):
        self.npp = NetworkPacketsProcessor()

    def test_case_1(self):
        #test empty input
        # given
        self.buffer_size = 1
        self.packets = []
        expected_result = []  # Ожидаемое время начала обработки пакетов

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, len(self.packets))

        # then
        self.assertEqual(result, expected_result)

    def test_2(self):
        # given
        self.buffer_size = 1
        self.packets = [[0, 0]]
        expected_result = ['0']  # Ожидаемое время начала обработки пакетов

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, len(self.packets))

        # then
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        # given
        self.buffer_size = 1
        self.packets = [[0, 1], [1, 1]]
        expected_result = ['0', '1']  # Все пакеты могут быть обработаны

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, len(self.packets))

        # then
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        # given
        self.buffer_size = 1
        self.packets = [[0, 1], [2, 1]]
        expected_result = ['0', '2']  # Ожидаемое время начала обработки пакетов

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, len(self.packets))

        # then
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        # given
        self.buffer_size = 1
        self.packets = [[0, 1], [1, 1]]
        expected_result = ['0', '1']  # Невозможно обработать пакеты

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, len(self.packets))

        # then
        self.assertEqual(result, expected_result)

    def test_case_6(self):
        # given
        input_file = read_input(task=3)
        first_line = input_file[0].split()
        self.buffer_size = int(first_line[0])
        self.n = int(first_line[1])
        self.packets = [list(map(int, i.split())) for i in input_file[1:] if len(i.split()) == 2]
        expected_result = ['0', '3', '10']

        # when
        result = self.npp.network_packets(self.buffer_size, self.packets, self.n)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()