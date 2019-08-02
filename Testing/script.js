import {tween} from 'popmotion'

const counter = document.querySelector('#a .counter');
const updateCounter = (v) => counter.innerHTML = v;

tween().start(updateCounter);
