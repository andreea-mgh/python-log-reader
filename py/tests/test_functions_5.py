import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises5(unittest.TestCase):

    def test_most_succesful_runs(self):
        dict = ex5(extractData(readFile(testpath)))
        most_successful_runs_app, num_successful_runs = dict
        self.assertEqual(most_successful_runs_app, "BackendApp")
        self.assertEqual(num_successful_runs, 2)




if __name__ == '__main__':
    unittest.main()