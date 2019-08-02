let firstName = "Noah";
let lastName = "Krohngold";
let age = 17;


//function determining if user can drive based on their age
const canYouDrive = (personAge) => {
  if (personAge >=18) {
    return ("Congratulations! You can legally drive!");
  } else if (personAge >= 16) {
    return ("At " + personAge + " years old you can get a driver's permit. Get started!");
  } else if (personAge > 10 && personAge < 16) {
    return ("Sorry, you can't legally acquire a driver's license! You have to wait " + (18-personAge)
    + " more years before you can get a permit to start learning!");
  } else {
    return ("Sorry, that just doesn't make sense :/");
  }
};

canYouDrive(age);



//single-line comment

/*
Multi-line comment
*/
