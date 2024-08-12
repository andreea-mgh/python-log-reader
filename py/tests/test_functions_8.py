import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises8(unittest.TestCase):

    def test_most_active_hour_interval(self):
        logs = extractData(readFile(testpath))
        most_active_hour_interval = ex8(logs)
        self.assertEqual(most_active_hour_interval['API'], "02")
        self.assertEqual(most_active_hour_interval['Backend'], "00")
        self.assertEqual(most_active_hour_interval['Frontend'], "18")




if __name__ == '__main__':
    unittest.main()