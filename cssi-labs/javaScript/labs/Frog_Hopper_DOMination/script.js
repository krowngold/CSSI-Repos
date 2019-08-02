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

let currentlily = 1;
let invisCounter = 0;

const frogger = document.querySelector("#frog")/* Use a querySelector to grab your frog from your HTML */;

const header = document.querySelector("#header");
const loseHeader = document.querySelector("#loseHeader");
const lilypad1 = document.querySelector("#lilypad1");
const lilypad2 = document.querySelector("#lilypad2");
const lilypad3 = document.querySelector("#lilypad3");
const lilypad4 = document.querySelector("#lilypad4");
const lilypad5 = document.querySelector("#lilypad5");

if (currentlily === 1) {
  header.style.display = "none";
  loseHeader.style.display = "none";
}

setInterval(() => {
  if (invisCounter%2 === 0) {
    lilypad3.style.display = "none";
    if (currentlily === 3) {
      currentlily = 1;
      frogger.style.left = "17%";
      frogger.style.top = "50%";
      lilypad3.classList.remove("active");
      lilypad1.classList.add("active");
    }
  }
  else{
    lilypad3.style.display = "block";
  }
  invisCounter++;
}, 1000);



frogger.addEventListener("mouseover", (e) => {
  frogger.style.width = "80px";
  frogger.style.height = "80px";
});

// frogger.addEventListener

document.body.addEventListener("keydown",(e) => {
  if(e.key === " ") {
    console.log("Restarting!");
    lilypad1.classList.add("active");
    lilypad2.classList.remove("active");
    lilypad3.classList.remove("active");
    lilypad4.classList.remove("active");
    lilypad5.classList.remove("active");
    header.style.display = "none";
    frogger.style.left= "17%";
    frogger.style.top = "50%";
    currentlily=1;
  }
});

frogger.addEventListener("mouseleave", (e) =>  {
  frogger.style.width = "70px";
  frogger.style.height = "70px";
});

frogger.addEventListener("click", (e) => {
  // Insert what should happen when you click on the frog!
  if (currentlily === 1) {
    frogger.style.left = "33.5%";
    frogger.style.top = "24%";
    lilypad1.classList.remove("active");
    lilypad2.classList.add("active");
  }
  else if (currentlily === 2) {
    if (lilypad3.style.display === "none") {
      console.log("No lilypad found :(");
      currentlily = 1;
      frogger.style.left = "17%";
      frogger.style.top = "50%";
      lilypad2.classList.remove("active");
      lilypad1.classList.add("active");
    }
    else {
      frogger.style.left = "50%";
      frogger.style.top = "50%";
      lilypad2.classList.remove("active");
      lilypad3.classList.add("active");
    }
  }
  else if (currentlily === 3) {
      frogger.style.left = "68%";
      frogger.style.top = "75%";
      lilypad3.classList.remove("active");
      lilypad4.classList.add("active");

  }
  else if (currentlily === 4) {
    frogger.style.left = "83%";
    frogger.style.top = "50%";
    lilypad4.classList.remove("active");
    lilypad5.classList.add("active");
    header.style.display = "inline";
  }
  currentlily++;
});
