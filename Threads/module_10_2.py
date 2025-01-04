import threading
import time


class Knight(threading.Thread):
    """
    This is a class for creating game heroes - Knights. Every Knight creating as a new thread
    Attributes:
        enemies: number of enemy warriors, equal for each Knight
        delay: duration of the game day, equal for each Knight
    """
    enemies = 100
    delay = 1

    def __init__(self, name: str, power: int):
        """
        The constructor for Knight class.
        Parameters:
            name (str): name of the hero
            power (int): hero's power (the number of enemies hero can kill in 1 game day)
        """
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        """
        This method describes the mechanism of the battle.
        Every second, the number of enemies decreases by the amount of the hero's strength.
        Once the number of enemies decreases to zero, the battle ends and the stream closes.
        """
        days = 0
        print(f'{self.name}, we are under attack!')
        while self.enemies > 0:
            self.enemies -= self.power
            time.sleep(self.delay)
            days += self.delay
            print(f'{self.name} has been fighting for {days} days, {self.enemies} warriors left')
        print(f'{self.name} won after {days} days!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('\nAll battles are over!')
