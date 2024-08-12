import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises9(unittest.TestCase):

    def test_failure_rate_percentage(self):
        logs = extractData(readFile(testpath))
        failure_rate = ex9(logs)
        frontend_failure_rate = round(failure_rate['Frontend'], 2)
        backend_failure_rate = round(failure_rate['Backend'], 2)
        api_failure_rate = round(failure_rate['API'], 2)
        self.assertEqual(frontend_failure_rate, 33.33)
        self.assertEqual(backend_failure_rate, 25.0)
        self.assertEqual(api_failure_rate, 33.33)


if __name__ == '__main__':
    unittest.main()