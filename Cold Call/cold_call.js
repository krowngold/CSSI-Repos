const button = document.querySelector(".button");
const nameLabel = document.querySelector("#nameLabel");
let counter = 1;
let randNum = 0;
let students = ["Asia", "Daniela","Tjay","Sam","Asha","Isa","Gabriel","Mayra","Brian","Uyen","Daniela","Beth","D'angely","Erin","Isaac","Adam","Ashley","Alexa","Zachary","Jason","Jet","Taylor","Adan","Amankwah","Sydney","Ethan","Kennedy", "Iris", "Dalen"];
button.addEventListener("click", (e) => {
  let x = [];
  if (counter !== 0) {
    button.innerHTML = "Call for backup!";
  }
  console.log(students);
  randNum = Math.floor(Math.random()*students.length);
  nameLabel.innerHTML = students[randNum];
  students.forEach((student) => {
    if (student !== students[randNum]) {
      x.push(student);
    }
  });
  students = x;
  counter++;
});



nameLabel.style.fontFamily = "Times New Roman, Arial, sans-serif";
nameLabel.style.fontSize = "80px";
nameLabel.style.color = "beige";
button.style.width = "800px";
button.style.height = "100px";
button.style.fontFamily = "Times New Roman, Arial, sans-serif";
button.style.fontSize = "65px";
button.style.backgroundColor = "yellow";
document.body.style.backgroundColor = "lightcoral";
