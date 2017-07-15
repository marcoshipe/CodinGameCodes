import argparse
import unittest
from io import StringIO
from unittest.mock import patch


def main():
    r = int(input())  # The original number R of the sequence.
    l = int(input())  # The line L to display. The index of the first line is 1.
    conway_sequence_list = [r]
    for _ in range(l-1):
        conway_sequence_list = conway_sequence_get_next_line(conway_sequence_list)
    print(" ".join(str(x) for x in conway_sequence_list))


def conway_sequence_get_next_line(actual_line):
    actual_ch = actual_line[0]
    amount = 0
    next_line = []
    for ch in actual_line:
        if ch != actual_ch:
            next_line.append(amount)
            next_line.append(actual_ch)
            actual_ch = ch
            amount = 1
        else:
            amount += 1
    next_line.append(amount)
    next_line.append(actual_ch)
    return next_line


class MyTestCase(unittest.TestCase):
    def run_test_file(self, input_file_path, expected_output_file_path):
        with open(input_file_path, 'r') as input_file, open(expected_output_file_path, 'r') as expected_output_file:
            with patch('sys.stdin', input_file), patch('sys.stdout', new=StringIO()) as output:
                main()
                self.assertEqual(output.getvalue().strip(), expected_output_file.read())

    def test_r_1_l_11(self):
        self.run_test_file('test_r_1_l_11_input.txt', 'test_r_1_l_11_expected_output.txt')

    def test_r_2_l_1(self):
        self.run_test_file('test_r_2_l_1_input.txt', 'test_r_2_l_1_expected_output.txt')

    def test_r_5_l_10(self):
        self.run_test_file('test_r_5_l_10_input.txt', 'test_r_5_l_10_expected_output.txt')

    def test_r_25_l_10(self):
        self.run_test_file('test_r_25_l_10_input.txt', 'test_r_25_l_10_expected_output.txt')

    def test_r_1_l_25(self):
        self.run_test_file('test_r_1_l_25_input.txt', 'test_r_1_l_25_expected_output.txt')

    def test_r_33_l_25(self):
        self.run_test_file('test_r_33_l_25_input.txt', 'test_r_33_l_25_expected_output.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolution of \"Conway Sequence\" problem from codingame.com')
    parser.add_argument('--unittest', help='run unit tests', action='store_true')
    args = parser.parse_args()
    if args.unittest:
        unittest.main(argv=[argparse.ArgumentParser().prog])
    else:
        main()
