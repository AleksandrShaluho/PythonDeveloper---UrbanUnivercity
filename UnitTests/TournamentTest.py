import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Usane', 10)
        self.runner_2 = rt.Runner('Andrew', 2)
        self.runner_3 = rt.Runner('Nick', 15)

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_round_1(self):
        tournament = rt.Tournament(10, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results['test_1'] = results
        self.assertTrue(results[max(results)] == 'Andrew')

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_round_2(self):
        tournament = rt.Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results['test_2'] = results
        self.assertTrue(results[max(results)] == 'Andrew')

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_round_3(self):
        tournament = rt.Tournament(5200, self.runner_1, self.runner_2)
        results = tournament.start()
        self.all_results['test_3'] = results
        self.assertTrue(results[max(results)] == 'Andrew')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(cls.all_results[result])


if __name__ == '__main__':
    unittest.main()
