import unittest
from functions import *
from readfile import *

testpath = "test_logs.txt"

class TestExercises7(unittest.TestCase):

    def test_longest_and_shortest_successful_run_times(self):
        logs = extractData(readFile(testpath))
        shortest_runtime_api, shortest_runtime_backend, shortest_runtime_frontend, longest_runtime_api, longest_runtime_backend, longest_runtime_frontend = ex7(logs)
        shortest_runtime_api = shortest_runtime_api[0]["run_time"]
        shortest_runtime_backend = shortest_runtime_backend[0]["run_time"]
        shortest_runtime_frontend = shortest_runtime_frontend[0]["run_time"]
        longest_runtime_api = longest_runtime_api[0]["run_time"]
        longest_runtime_backend = longest_runtime_backend[0]["run_time"]
        longest_runtime_frontend = longest_runtime_frontend[0]["run_time"]
        self.assertEqual(shortest_runtime_api, "20")
        self.assertEqual(shortest_runtime_backend, "16")
        self.assertEqual(shortest_runtime_frontend, "25")
        self.assertEqual(longest_runtime_api, "20")
        self.assertEqual(longest_runtime_backend, "16")
        self.assertEqual(longest_runtime_frontend, "25")


if __name__ == '__main__':
    unittest.main()