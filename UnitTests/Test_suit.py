import unittest
import RunnerTest
import TournamentTest

my_tests = unittest.TestSuite()
my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

tests_runner = unittest.TextTestRunner(verbosity=2)
tests_runner.run(my_tests)
