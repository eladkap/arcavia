var canvas = document.getElementById('gameplay-canvas1');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

/* GLOBALS */
var bubbles = [];
var queries = [];

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
    checkClicks(mx, my);
}

/* PRELOAD METHODS */
function loadQueries() {

}

/* SETUP METHODS */
function createBubbles() {
    for (let i = 0; i < SYMBOLS.length; i++) {
        let x = Utils.getRandomFromRange(2 * BUBBLE_RADIUS, window.innerWidth - 2 * BUBBLE_RADIUS);
        let y = Utils.getRandomFromRange(2 * BUBBLE_RADIUS, window.innerHeight - 2 * BUBBLE_RADIUS);
        let angle = Math.random() * (2 * Math.PI);
        let velocity = Vector.fromAngle(angle, BUBBLE_MAX_VELOCITY);
        let radius = BUBBLE_RADIUS;
        let color = COLORS[0];
        let symbol = SYMBOLS[i];
        let srcImage = null;
        let bubble = new Bubble(x, y, radius, velocity, color, symbol, srcImage);
        bubbles.push(bubble);
    }
}

/* UPDATE METHODS */
function updateBubbles() {
    for (let i = 0; i < bubbles.length; i++) {
        bubbles[i].display();
        bubbles[i].update();
    }
}

function showWindowSize() {
    ctx.font = `${FONTS_SIZE_S}px ${FONT_FAMILY}`;
    ctx.fillStyle = 'white';
    ctx.fillText(`[${window.innerWidth} x ${window.innerHeight}]`, 10, window.innerHeight - 20);
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

function checkClicks(mx, my) {
    for (let i = 0; i < bubbles.length; i++) {
        if (bubbles[i].isClicked(mx, my)) {
            bubbles.splice(i, 1);
        }
    }
}
  
function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    showWindowSize();
    /* update entities */
    updateBubbles();

    /* check mouse events */
    requestAnimationFrame(update);
  }

function runGame() {
    console.log('runGame');
    setup();
    requestAnimationFrame(update);
}

preload(runGame);
