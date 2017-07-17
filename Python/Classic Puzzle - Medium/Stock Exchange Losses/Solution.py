import argparse
import unittest
from io import StringIO
from unittest.mock import patch


def main():
    # The idea is keep track of the actual slope as long as the actual point is under the initial point
    # And keep the deepest slope
    # When a slope end, i save it only if is the deepest one, and start a new one

    _ = int(input())

    actual_max = 0
    actual_min = 0
    max_dif = 0
    prev = 0

    for i in input().split():
        i = int(i)
        if i <= prev:
            # going down
            if i < actual_min:
                actual_min = i
        else:
            if i > actual_max:
                if (actual_min - actual_max) < max_dif:
                    max_dif = actual_min - actual_max
                actual_max = i
                actual_min = i
        prev = i

    if (actual_min - actual_max) < max_dif:
        max_dif = actual_min - actual_max

    print(str(max_dif))


class MyTestCase(unittest.TestCase):
    def run_test_file(self, input_file_path, expected_output_file_path):
        with open(input_file_path, 'r') as input_file, open(expected_output_file_path, 'r') as expected_output_file:
            with patch('sys.stdin', input_file), patch('sys.stdout', new=StringIO()) as output:
                main()
                self.assertEqual(output.getvalue().strip(), expected_output_file.read())

    def test_example_1(self):
        self.run_test_file('test_example_1_input.txt', 'test_example_1_expected_output.txt')

    def test_example_2(self):
        self.run_test_file('test_example_2_input.txt', 'test_example_2_expected_output.txt')

    def test_example_3(self):
        self.run_test_file('test_example_3_input.txt', 'test_example_3_expected_output.txt')

    def test_example_4(self):
        self.run_test_file('test_example_4_input.txt', 'test_example_4_expected_output.txt')

    def test_example_5(self):
        self.run_test_file('test_example_5_input.txt', 'test_example_5_expected_output.txt')

    def test_example_6(self):
        self.run_test_file('test_example_6_input.txt', 'test_example_6_expected_output.txt')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolution of \"Stock Exchange Losses\" problem from codingame.com')
    parser.add_argument('--unittest', help='run unit tests', action='store_true')
    args = parser.parse_args()
    if args.unittest:
        unittest.main(argv=[argparse.ArgumentParser().prog])
    else:
        main()
