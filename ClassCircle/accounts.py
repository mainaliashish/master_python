import datetime
import pytz


class Account():

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance, type):
        self._name = name
        self.__balance = balance
        self._type = type
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {} as a {} Account".format(self._name, self._type))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The withdraw amout is greater than initial balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is Rs.{} in {} Account".format(self.__balance, self._type))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:7} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))




if __name__ == '__main__':
    ashish = Account("Ashish", 400, "Saving")
    ashish.show_balance()

    ashish.deposit(1000)

    # ashish.withdraw(30000)
    ashish.withdraw(400)
    ashish.show_transactions()
# ram = Account("Ram", 3000)
# ram.show_balance()
