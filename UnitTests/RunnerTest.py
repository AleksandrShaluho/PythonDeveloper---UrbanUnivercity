import unittest
from sys import exc_info
import runner_and_tournament as rt
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_walk(self):
        try:
            my_runner = rt.Runner('Bolt', -5)
            for _ in range(10):
                my_runner.walk()
            self.assertEqual(my_runner.distance, 50)
            logging.info("test_walk executed successfully", exc_info=True)
        except ValueError:
            logging.warning(f'Incorrect speed value for runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_run(self):
        try:
            my_runner = rt.Runner(2, 7)
            for _ in range(10):
                my_runner.run()
            self.assertEqual(my_runner.distance, 100)
        except TypeError:
            logging.warning('Incorrect type for runner name', exc_info=True)

    @unittest.skipIf(is_frozen, 'Tests in this tests case have been frozen')
    def test_challenge(self):
        my_runner = rt.Runner('Bolt',5)
        alien_runner = rt.Runner('Brezhnev',2)
        for _ in range(10):
            my_runner.run()
            alien_runner.walk()
        self.assertNotEqual(my_runner.distance, alien_runner.distance)


if __name__ == '__main__':
    unittest.main()
