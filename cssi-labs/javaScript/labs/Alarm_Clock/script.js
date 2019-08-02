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
let date = new Date();
let am = true;
let alarmTime;

console.log(date.toLocaleTimeString());

  // button.addEventListener("onclick", setAlarm());

//parses and returns the time from the timeInput textarea
// const parseTime = (input) => {
//   let newString = "";
//   for (let c = 0; c < input.length; c++) {
//     if (!isNaN(input.charAt(c))) {
//         newString = newString + input.charAt(c);
//     }
//   }
//   for (let c = 0; c < input.length; c++) {
//     if (input.charAt(c) === "a") {
//       am = true;
//
//     }
//     else if (input.charAt(c) === "p") {
//       am = false;
//       //new function to add 12 hours to the time, if hours = 24 change to 23
//     }
//   }
//
//   return newString;
// };


//searches the user's input for the hour they want to wake up at
const parseHours = (input) => {
  let divLocation = 0;
  if (input.charAt(1) === ":") {
    return input.charAt(0);
  }
  else if (input.charAt(2) === ":") {
    return input.charAt(0) + input.charAt(1);
  }
}

const parseMinutes = (input) => {
  let divLocation = 0;
  if (input.charAt(1) === ":") {
    return input.charAt(2) + input.charAt(3);
  }
  else if (input.charAt(2) === ":") {
    return input.charAt(3) + input.charAt(4);
  }
}

const compareTimes = (current, alarm) => {

};


//FUNCTIONS QUIZ ANSWERS: 3, 1,


// setInterval(() => {
//   console.log("Wake up!");
// }, 3000)


const setTime = () => {
  console.log("Starting setTime() function!");
  // alarmTime = parseTime(document.getElementById('timeInput').value);
  // console.log("The chosen alarm time is " + alarmTime);

  console.log("The hours you're waking up at is " + parseHours(document.getElementById
  ('timeInput').value));
}

const myAlarm = (wakeTime) => {
  // return "Hey, Noah, wake up! It's " + date.toTimeString();
  return "Hey, Noah, wake up! It's " + wakeTime;
};

const momAlarm = (wakeTime) => {
  // return "Hey, Mom, wake up! It's " + date.toTimeString();
  return "Hey, Mom, wake up! It's " + wakeTime;
};

const familyAlarm = (wakeTime, person) => {
  // return "Hey, " + person + ", wake up! It's " + date.toTimeString();
  return "Hey, " + person + ", wake up! It's " + wakeTime;
};

const importantAlarm = (message) => {
  return message.toUpperCase();
};

const snoozeAlarm = (wakeTime) => {
  return "The alarm for " + wakeTime + " has been changed to " + (wakeTime + 1);
};

const multAlarm = (numPeople) => {
  // for(let i = 0; i<numPeople; i++) {
  //   console.log("Wake up!");
  // }
  console.log(("Wake up!").repeat(numPeople));
};
