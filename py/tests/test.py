import unittest
from functions import *
from readfile import *

testpath = "example.txt"

class TestExercises(unittest.TestCase):

    #test for the ex1
    def test_should_verify_the_number_of_info_API(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("INFO").get("API"), 1)

    def test_should_verify_the_number_of_error_API(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("ERROR").get("API"), 1)

    def test_should_verify_the_number_of_debug_API(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("DEBUG").get("API"), 1)

    def test_should_verify_the_number_of_info_BackendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("INFO").get("Backend"), 2)

    def test_should_verify_the_number_of_error_BackendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("ERROR").get("Backend"), 1)

    def test_should_verify_the_number_of_debug_BackendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("DEBUG").get("Backend"), 1)

    def test_should_verify_the_number_of_info_FrontendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("INFO").get("Frontend"), 1)

    def test_should_verify_the_number_of_error_FrontendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("ERROR").get("Frontend"), 1)

    def test_should_verify_the_number_of_debug_FrontendApp(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("DEBUG").get("Frontend"), 1)

    def test_should_verify_the_number_of_info_SYSTEM(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("INFO").get("System"), 1)

    def test_should_verify_the_number_of_error_SYSTEM(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("ERROR").get("System"), 2)

    def test_should_verify_the_number_of_debug_SYSTEM(self):
        dict = ex1(extractData(readFile(testpath)))
        self.assertEqual(dict.get("DEBUG").get("System"), 1)
##############################################################################################################

    #test for the ex2
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

##############################################################################################################
    #test for the ex3
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

# test for the ex4
    def test_most_errors(self):
        dict = ex4(extractData(readFile(testpath)))
        #self.assertEqual(dict.get("ERROR").get("System"), 2)
        most_failed_app, num_failures = dict
        self.assertEqual(most_failed_app, "System")
        self.assertEqual(num_failures, 2)

# test for the ex5
    def test_most_succesful_runs(self):
        dict = ex5(extractData(readFile(testpath)))
        most_successful_runs_app, num_successful_runs = dict
        self.assertEqual(most_successful_runs_app, "BackendApp")
        self.assertEqual(num_successful_runs, 2)


# test for the ex 6
    def test_failed_runs_time_interval(self):
         result = ex6(extractData(readFile(testpath)))
         self.assertEqual(result, 3)  # Assuming 08:00:00-15:59:59 has the most failed runs




    # test for ex 7
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
    # test for ex 8
    def test_most_active_hour_interval(self):
        logs = extractData(readFile(testpath))
        most_active_hour_interval = ex8(logs)
        self.assertEqual(most_active_hour_interval['API'], "02")
        self.assertEqual(most_active_hour_interval['Backend'], "00")
        self.assertEqual(most_active_hour_interval['Frontend'], "18")


    # test for ex 9
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