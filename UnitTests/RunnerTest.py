import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Tests in this tests case have been frozen')
    def test_walk(self):
        my_runner = runner.Runner('Bolt')
        for _ in range(10):
            my_runner.walk()
        self.assertEqual(my_runner.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Tests in this tests case have been frozen')
    def test_run(self):
        my_runner = runner.Runner('Bolt')
        for _ in range(10):
            my_runner.run()
        self.assertEqual(my_runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Tests in this tests case have been frozen')
    def test_challenge(self):
        my_runner = runner.Runner('Bolt')
        alien_runner = runner.Runner('Brezhnev')
        for _ in range(10):
            my_runner.run()
            alien_runner.walk()
        self.assertNotEqual(my_runner.distance, alien_runner.distance)


if __name__ == '__main__':
    unittest.main()
