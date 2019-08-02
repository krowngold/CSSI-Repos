// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customerName;
let balance;
let loggedIn = false;
let password = "";

const openAccount = (name, startBalance = 0, pass) => {
  balance = startBalance;
  customerName = name;
  password = pass;
  return customerName + " has opened a new account with a balance of $" + balance; //write the statment you need to return here
};

const logIn = (name, pass) => {
  if(name === customerName && pass === password) {
    loggedIn = true;
    return customerName + " has logged in.";
  }
  else {
    loggedIn = false;
    return "Incorrect credentials.";
  }
};

const logOut = () => {
  loggedIn = false;
  return customerName + " has logged out.";
};

const appropriateName = () => {
    console.log(openAccount("Noah", 300));
    console.log(deposit(50));
    console.log(withdraw(500));
};

const getBalance = () => {
  return balance;
}

const deposit = (value) => {
  if (loggedIn === false) {
    return "Please log in first.";
  }
  else {
    balance += value;
    return customerName + " has deposited $" + value + ". "+ customerName +"'s total balance is $" + balance;

  }
};

const withdraw = (value) => {
  if (balance - value < 0) {
    return "Sorry. You don't have enough money in your account to withdraw." +
    " You need $" + (value-balance) + " more to make a withdrawal of that size.";
  }
  else if (loggedIn === false) {
    return "Please log in first.";
  }
  else {
    balance -= value;
    return customerName + " has withdrawn $" + value + ". "
    + customerName + " has $" + balance + " remaining";
  }
};

// Write your script below
console.log("script is running...");
