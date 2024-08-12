import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises6(unittest.TestCase):

    def test_failed_runs_time_interval(self):
         result = ex6(extractData(readFile(testpath)))
         self.assertEqual(result, 3)  # Assuming 08:00:00-15:59:59 has the most failed runs




if __name__ == '__main__':
    unittest.main()