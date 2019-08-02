import time

#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    balance = 0
    label = ""

    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return '{self.label}\'s bank account. The balance is {self.balance}.'.format(self=self)

    def withdraw(self, amount):
        if (self.balance - amount < 0 or amount < 0):
            amount = 0
        self.balance = self.balance - int(amount)
        self.transactions.append(Transaction(time.time(), "withdrawal", amount, self.label, "None"))
        print "The new balance is " + str(self.balance)

    def deposit(self, amount):
        if (amount < 0):
            amount = 0
        self.balance+=amount
        self.transactions.append(Transaction(time.time(), "deposit", amount, self.label, "None"))
        print "The new balance is " + str(self.balance)

    def rename(self, name):
        if (name == ""):
            name = "real acc"
        self.label=name

    def transfer(self, dest_account, amount):
        if (amount > self.balance):
            amount = 0
        elif (amount < 0):
            amount = 0
        dest_account.deposit(amount)
        self.balance = self.balance - amount
        self.transactions.append(Transaction(time.time(), "deposit", amount, self.label, "None"))

    def listTransactions(self):
        print(str(self.transactions))
    pass


class Transaction(object):
    def __init__(self, time, type, amount, account, dest_account):
        self.time = time
        self.type = type
        self.amount = amount
        self.account = account
        self.dest_account = dest_account
        if (self.type == "withdrawal"):
            self.__str__ = str(self.time) + ": withdraw $" + str(self.amount)
        elif (self.type == "deposit"):
            self.__str__ = str(self.time) + ": deposit $" + str(self.amount)
        else:
            self.__str__ = str(self.time) + ": transfer $" + str(self.amount) + " to account \'" + str(self.dest_account) +"\'"
