import requests
import json


class Exchanger:
    user_currency = "XXX"
    desired_currency = None
    cash = 0
    base_currencies = ["USD", "EUR"]
    rates = {}
    json_data = {}
    connection = None
    decision = None

    def is_your_currency_correct(self):
        while 1:
            self.user_currency = input("What's your currency? ==> ")
            try:
                self.connect()
            except json.decoder.JSONDecodeError:
                print("Your currency doesn't exist!")
            else:
                break

    def connect(self):
        url = f"http://www.floatrates.com/daily/{self.user_currency.lower()}.json"
        self.connection = requests.get(url)
        self.json_data = self.connection.json()

    def dict_print(self):
        for value in self.rates:
            print(f"{self.rates[value]}\t\t{value}")

    def display_menu(self):
        self.decision = input("1: convert next value, 2: see the cache, other: exit ==> ")

    def check_number(self):
        while 1:
            try:
                self.cash = float(input("How much money do you want to covert? ==> "))
            except ValueError:
                print("This is not a number!")
            else:
                break

    def get_user_data(self):
        while 1:
            self.desired_currency = input("What currency do you want? ==> ").lower()
            if self.desired_currency in self.json_data:
                self.check_number()
                break
            else:
                print("Your desired currency is wrong!")

    def get_rates(self):
        self.rates = {rate.upper(): self.json_data[rate]["rate"] for rate in self.json_data if
                      rate.upper() in self.base_currencies}

    def is_in_cache(self):
        print("Checking the cache...")
        return self.desired_currency.upper() in self.base_currencies

    def add_rate(self):
        code = self.desired_currency
        rate = self.json_data[code.lower()]["rate"]
        self.rates.update({code.upper(): rate})

    def print_rate(self):
        code = self.desired_currency.upper()
        print(f"{self.cash} {self.user_currency.upper()} ==> {format(self.cash * self.rates[code], '.2f')} {code}.")

    def exchange_money(self):
        if self.is_in_cache():
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            self.add_rate()
            self.base_currencies.append(self.desired_currency.upper())
        self.print_rate()

    def __init__(self):
        self.is_your_currency_correct()
        self.connect()
        while True:
            self.display_menu()
            if self.decision == '1':
                self.get_user_data()
                self.get_rates()
                self.exchange_money()
            elif self.decision == '2':
                self.dict_print()
            else:
                break


Exchanger()

