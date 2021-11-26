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

    def get_user_input(self):
        self.desired_currency = input("What currency do you want? ==> ")
        self.cash = float(input("How much money do you want to covert? ==> "))

    def is_currency_correct(self, currency):
        self.json_data = self.connection.json()
        if currency:
            return self.desired_currency in self.json_data
        else:
            return self.user_currency in self.json_data

    def connect(self):
        url = f"http://www.floatrates.com/daily/{self.user_currency.lower()}.json"
        self.connection = requests.get(url)

    def get_rates(self):
        self.rates = {rate.upper(): self.json_data[rate]["rate"] for rate in self.json_data if rate.upper() in self.base_currencies}

    def add_rate(self):
        code = self.desired_currency
        rate = self.json_data[code.lower()]["rate"]
        self.rates.update({code.upper(): rate})

    def print_rate(self):
        code = self.desired_currency.upper()
        print(f"{self.cash} {self.user_currency.upper()} ==> {format(self.cash * self.rates[code], '.2f')} {code}.")

    def is_in_cache(self):
        print("Checking the cache...")
        return self.desired_currency.upper() in self.base_currencies

    def __init__(self):
        self.connect()
        while not self.is_currency_correct(0):
            self.user_currency = input("What currency do you have? ==> ")
        while 1:
            d = input("1: convert next value, 2: see the cache, other: exit ==> ")
            if d == '1':
                self.get_user_input()
                self.connect()
                self.get_rates()
                if self.is_currency_correct(1):
                    if self.is_in_cache():
                        print("Oh! It is in the cache!")
                    else:
                        print("Sorry, but it is not in the cache!")
                        self.add_rate()
                        self.base_currencies.append(self.desired_currency.upper())
                    self.print_rate()
                else:
                    print("Wrong currency!")
            elif d == '2':
                print(self.rates)
            else:
                break


Exchanger()
