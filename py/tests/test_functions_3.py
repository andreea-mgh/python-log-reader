import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises3(unittest.TestCase):

    def test_should_verify_the_number_of_failed_runs_for_frontend(self):
        a = ex3(extractData(readFile(testpath)))
        self.assertEqual(a[0], 1)
    def test_should_verify_the_number_of_failed_runs_for_backend(self):
        a = ex3(extractData(readFile(testpath)))
        self.assertEqual(a[1], 1)

    def test_should_verify_the_number_of_failed_runs_for_api(self):
        a = ex3(extractData(readFile(testpath)))
        self.assertEqual(a[2], 1)

    def test_should_verify_the_number_of_failed_runs_for_system(self):
        a = ex3(extractData(readFile(testpath)))
        self.assertEqual(a[3], 2)



if __name__ == '__main__':
    unittest.main()