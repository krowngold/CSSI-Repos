const headerElement = document.querySelector('#header');
// headerElement.style.color = 'red';

const subheaderElement = document.querySelector('#subheader');

subheaderElement.addEventListener('mouseover', () => {
  let hue = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ','
  + (Math.floor(Math.random() * 256)) + ')';
  // console.log("headerElement");
  subheaderElement.style.color = hue;
});

subheaderElement.classList.add('blueText');

subheaderElement.addEventListener('mouseleave', () => {
  let hue = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ','
  + (Math.floor(Math.random() * 256)) + ')';
  // console.log("headerElement");
  subheaderElement.style.color = hue;
});

setInterval( () => {
  let hue = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ','
  + (Math.floor(Math.random() * 256)) + ')';
  // console.log("headerElement");
  headerElement.style.color = hue;
}, 5000);
