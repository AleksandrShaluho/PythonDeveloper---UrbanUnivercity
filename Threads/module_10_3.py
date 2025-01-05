from threading import Lock, Thread
from random import randint
from time import sleep
from datetime import datetime


class Bank:
    """
    This class is designed to simulate the movement of funds on the account: deposits and withdrawals.
    Withdrawals are blocked when a request is made for an amount greater than the balance
    and are unblocked when the balance reaches 500.

    Attributes of instance:
        balance (int): current balance of virtual 'account' with initial value = 0
        lock (Lock): special object which block thread with specific type of fund's movement
    """

    def __init__(self):
        """
        The constructor. Creates virtual 'account' with initial balance and locker.
        """
        self.balance: int = 0
        self.lock = Lock()

    def deposit(self) -> None:
        """
        A method for simulating the deposit of a virtual account,
        making 100 transactions for a random amount from 50 to 500.
        If the account balance reaches 500, withdrawal transactions are unblocked.
        """
        transactions_count = 1
        while transactions_count <= 100:
            deposit = randint(50, 500)
            self.balance += deposit
            print(
                f'Пополнение: {deposit}. Баланс - {self.balance} (id транзакции D{transactions_count}), время: {self.__timestamp()}')
            transactions_count += 1
            # Цитирую условие задачи: "Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его
            # методом release. Приведенный в задаче пример вывода на консоль не соответствует этому условию, так как в примере снятие
            # блокировки производится без учета условия "баланс больше или равен 500 И..". См. например строки вывода 5-8
            # задачу решил в соответствии с условием, несмотря на несоответствие примеру вывода на консоль
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)

    def take(self) -> None:
        """
        A method for simulating the withdrawal of a virtual account,
        making 100 transactions for a random amount from 50 to 500.
        If the withdrawal request exceeds the balance on the account, withdrawal transactions are blocked.
        """
        transactions_count = 1
        while transactions_count <= 100:
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            # по условиям задачи блокировка производится при любой попытке снять больше, чем остаток. Даже если баланс 499, а снять пытались 500.
            if self.balance < withdraw:
                # снятия, то есть уменьшения не произошло, значит транзакции не было, поэтому счетчик транзакций не изменяется
                # цитата:"...100 транзакций снятия. Снятие - это уменьшение баланса..."
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= withdraw
                print(
                    f'Снятие: {withdraw}. Баланс: {self.balance} (id транзакции W{transactions_count}, время: {self.__timestamp()})')
                transactions_count += 1

    @staticmethod
    def __timestamp() -> str:
        return datetime.now().strftime('%F %T.%f')


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
