import argparse
import unittest
from io import StringIO
from unittest.mock import patch


def main():
    n = int(input())  # number of horses
    horses_strengths = []  # [horse_strength_1, horse_strength_2, ...]
    for i in range(n):
        horses_strengths.append(int(input()))

    horses_strengths.sort()
    min_dist = horses_strengths[1] - horses_strengths[0]
    for i in range(2, len(horses_strengths)):
        act_dist = horses_strengths[i] - horses_strengths[i - 1]
        if act_dist < min_dist:
            min_dist = act_dist

    print(str(min_dist))


class MyTestCase(unittest.TestCase):
    def run_test_file(self, input_file_path, expected_output_file_path):
        with open(input_file_path, 'r') as input_file, open(expected_output_file_path, 'r') as expected_output_file:
            with patch('sys.stdin', input_file), patch('sys.stdout', new=StringIO()) as output:
                main()
                self.assertEqual(output.getvalue().strip(), expected_output_file.read())

    def test_simple_test(self):
        self.run_test_file('test_simple_test_input.txt', 'test_simple_test_expected_output.txt')

    def test_horses_in_any_order(self):
        self.run_test_file('test_horses_in_any_order_input.txt', 'test_horses_in_any_order_expected_output.txt')

    def test_many_horses(self):
        self.run_test_file('test_many_horses_input.txt', 'test_many_horses_expected_output.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolution of \"Horse-racing Duals\" problem from codingame.com')
    parser.add_argument('--unittest', help='run unit tests', action='store_true')
    args = parser.parse_args()
    if args.unittest:
        unittest.main(argv=[argparse.ArgumentParser().prog])
    else:
        main()
