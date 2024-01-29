var canvas = document.getElementById('gameplay-canvas1');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

/* GLOBALS */
var bubbles = [];

/* KEYBOARD EVENTS */
// window.addEventListener("keypress", keyPressed);
window.addEventListener("keydown", keyDown);

/* MOUSE EVENTS */
window.addEventListener("click", onMouseClicked);

/* EVENT HANDLERS */
function keyPressed(event) {
    let key = event.key;
    console.log(`Key pressed: ${key}`);
}

function keyDown(event) {
    let key = event.key;
    console.log(`Key down: ${key}`);
}

function onMouseClicked(event) {
    let mx = event.clientX;
    let my = event.clientY;
    console.log(`clicked point: (${mx}, ${my})`);
}

/* PRELOAD METHODS */
function loadQueries() {

}

/* SETUP METHODS */
function createBubbles() {

}

/* UPDATE METHODS */
function updateBubbles() {
    
}

async function preload(callback) {
    console.log('preload');
    callback();
}

function setup() {
    console.log('setup');
    /* create entities */
    createBubbles();
}
  
  function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    /* update entities */
    updateBubbles();
    requestAnimationFrame(update);
  }

function runGame() {
    console.log('runGame');
    setup();
    requestAnimationFrame(update);
}

preload(runGame);
