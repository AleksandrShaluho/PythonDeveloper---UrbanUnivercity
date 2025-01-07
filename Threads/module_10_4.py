"""The module is designed to simulate the work of a cafe"""

import threading
import queue
from time import sleep
from random import randint


class Table:
    """
    Class for storing the state of a table - occupancy by guests
    Class instance attributes:
        number (int): number of a table
        guest (Guest): the guest who is sitting at this table (default - None)
    """

    def __init__(self, number: int) -> None:
        """
        The constructor for creating tables.
        Parameters:
            number (int): number of a table
        """
        self.number = number
        self.guest: Guest = None


class Guest(threading.Thread):
    """ Class for storing names of guests
        Class instance attributes:
            name (str): name of the guest
    """

    def __init__(self, name: str) -> None:
        threading.Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        """method for simulate time during which guest is sitting at this table."""
        sleep(randint(3, 10))


class Cafe:
    """
      Class for simulate the serve of guests.
      Class instance attributes:
          tables (tuple of Table objects): all tables in cafe
          queue (Queue): queue for guests who didn't have a table
      """

    def __init__(self, *tables: tuple[Table, ...]) -> None:
        """
        The constructor for creating tables.
        Parameters:
            tables (tuple of Table objects): collection of all tables in the cafe
        """
        self.tables = tables
        self.queue = queue.Queue()

    def guests_arrival(self, *guests: Guest) -> None:
        """
        Method for assigning arriving guests to tables or into a queue.
        Parameters:
            guests (Guest): any collection of guests names
        """
        for guest in guests:
            if next((table for table in self.tables if table.guest is None), None) is None:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
            else:
                free_table = next((table for table in self.tables if table.guest is None), None)
                free_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                free_table.guest.start()

    def discuss_guest(self) -> None:
        """
        Method for serving guests to tables or into a queue.
        Guests are served until the queue is empty or at least one table is occupied.
        """
        while (not self.queue.empty()) or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал (-а) и ушел (ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Armen', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guests_arrival(*guests)
cafe.discuss_guest()
