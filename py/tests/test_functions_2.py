import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises2(unittest.TestCase):

    def test_should_verify_average_successful_time_for_frontend(self):
        vect = ex2(extractData(readFile(testpath)))
        self.assertEqual(vect[0], 1)
        self.assertEqual(vect[1], 25.0)
    def test_should_verify_average_successful_time_for_backend(self):
        vect = ex2(extractData(readFile(testpath)))
        self.assertEqual(vect[2], 2)
        self.assertEqual(vect[3], 16.0)
    def test_should_verify_average_successful_time_for_api(self):
        vect = ex2(extractData(readFile(testpath)))
        self.assertEqual(vect[4], 1)
        self.assertEqual(vect[5], 20.0)



if __name__ == '__main__':
    unittest.main()