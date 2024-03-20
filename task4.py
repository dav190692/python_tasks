import random
from datetime import datetime
import pytz



class Person:
    def __init__ (self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    @property
    def first_name (self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Please type corect value for first name')
        self.__first_name = value

    @property
    def last_name (self):
        return self.__last_name
    
    @last_name.setter
    def last_name (self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Please type corect value for last name')
        self.__last_name = value

    @property
    def age (self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0 or not value or not isinstance(value, int):
            raise ValueError('Please type corect value for age')
        self.__age = value
        
    @property
    def address (self):
        return self.__address
    
    @address.setter
    def address (self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Please type corect value for address')
        self.__address = value

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Time:
    def __init__(self, prefered_tz):
        self.prefered_tz = prefered_tz

    @property
    def prefered_tz(self):
        return self.__prefered_tz
    
    @prefered_tz.setter
    def prefered_tz(self, tz):
        if tz in self.show_tz():
            self.__prefered_tz = tz
        else:
            tz = None
        

    def get_local_time(self):
        utc_timezone = pytz.utc
        current_utc_time = datetime.now(utc_timezone)
        return current_utc_time

    

    def show_tz (self):
        all_timezones = pytz.all_timezones
        return all_timezones



class BankAcount(Person, Time):
    interest_rate = 1
    transaction_id = 0
    account_number_cash = {}
    def __init__(self, first_name : str, last_name : str, age  : int, address : str, prefered_tz, starting_balance = 1000 ) -> None:
        super().__init__( first_name, last_name, age, address)
        Time.__init__(self, prefered_tz)
        self.__account_number = self._generate_account_number()
        self.__starting_balance = self._validate_starting_balance(starting_balance)


    @property
    def starting_balance(self):
        return self.__starting_balance
    

    def _validate_starting_balance(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError('Type corect value for starting balance')
        return value

    
    @property
    def account_number (self):
        return self.__account_number


    def _generate_account_number(self):
        number = random.randint(100000, 999999)
        if number not in self.account_number_cash:
            self.account_number_cash[number] = number
            return number
        else:
            return self._generate_account_number()
        
           



    def deposit(self, amount):
        if amount > 0 and isinstance(amount, int):
            self.__starting_balance += amount
            BankAcount.transaction_id += 1
            return self._generate_confirmation("D")
        else:
            return self._generate_confirmation("X")

        


    def withdraw(self, amount):
        if 0 < amount < self.__starting_balance:
            self.__starting_balance -= amount
            BankAcount.transaction_id += 1
            return self._generate_confirmation("W")
        else:
            return self._generate_confirmation("X")
        

    def pay_interest(self):
        interest_amount = (self.__starting_balance * BankAcount.interest_rate) / 100
        self.__starting_balance += interest_amount
        BankAcount.transaction_id += 1
        return self._generate_confirmation("I")

    def _generate_confirmation(self, transaction_type):
        time_utc = self.get_local_time().strftime('%Y%m%d%H%M%S')
        confirmation_number = f"{transaction_type}-{self.account_number}-{time_utc}-{BankAcount.transaction_id}"
        return confirmation_number
    
    def parse_confirmation_number(self, confirmation_number):
        items = confirmation_number.split('-')
        if len(items) != 4:
            return None
        
        transaction_type, account_number, time_utc, transaction_id = items

        time_utc = datetime.strptime(time_utc, '%Y%m%d%H%M%S')
        time_utc = pytz.utc.localize(time_utc)

        if self.prefered_tz:
            #  print('Yes ')
             local_timezone = pytz.timezone(self.prefered_tz)
            #  print(local_timezone)
             timestamp_local = time_utc.astimezone(local_timezone)
            #  print(timestamp_local)
        else:
             timestamp_local = time_utc


        result = {
        'account_number': int(account_number),
        'transaction_code': str(transaction_type),
        'transaction_id': int(transaction_id),
        'time_utc': time_utc,
        'time_local': timestamp_local.strftime('%Y-%m-%d %H:%M:%S'),
        }

        return result     

        




    

account1 = BankAcount("Davit", "Kirakosyan", 31, "Adraniki 148/9", 'Asia/Yerevan')




withdraw_confirmation = account1.withdraw(800)
deposit_confirmation = account1.deposit(123)
pay_interest_confirmation = account1.pay_interest()


print(withdraw_confirmation)
print(deposit_confirmation)
print(pay_interest_confirmation)
print(account1.starting_balance)


print(account1.parse_confirmation_number(withdraw_confirmation)['account_number'])
print(account1.parse_confirmation_number(withdraw_confirmation)['transaction_code'])
print(account1.parse_confirmation_number(withdraw_confirmation)['transaction_id'])
print(account1.parse_confirmation_number(withdraw_confirmation)['time_local'])
print(account1.parse_confirmation_number(withdraw_confirmation)['time_utc'])

print(account1.prefered_tz)















