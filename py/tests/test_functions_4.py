import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises4(unittest.TestCase):

    def test_most_errors(self):
        dict = ex4(extractData(readFile(testpath)))
        #self.assertEqual(dict.get("ERROR").get("System"), 2)
        most_failed_app, num_failures = dict
        self.assertEqual(most_failed_app, "System")
        self.assertEqual(num_failures, 2)


if __name__ == '__main__':
    unittest.main()