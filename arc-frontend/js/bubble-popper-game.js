var canvas = document.getElementById('bubble-popper-canvas');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
// canvas.width = 1024;
// canvas.height = 1280;

/* GLOBALS */
var bubbles = [];
var queries = [];

var dots = [];

/* KEYBOARD EVENTS */
// window.addEventListener("keypress", keyPressed);
window.addEventListener("keydown", keyDown);

/* MOUSE EVENTS */
window.addEventListener("click", onMouseClicked);

// window.addEventListener("mousemove", handleMouseMove);
// document.onmousemove = handleMouseMove;


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
    let canvasRect = canvas.getBoundingClientRect();
    let mousePos = Utils.translateMouseToCanvasPosition(event.pageX, event.pageY, canvasRect);
    checkClick(mousePos);

    // let canvasRect = canvas.getBoundingClientRect();
    // let mx = event.pageX - canvasRect.left - scrollX;
    // let my = event.pageY - canvasRect.top - scrollY;
    // checkClick(mx, my);
}

function onMouseOver(event) {
    let mx = event.clientX;
    let my = event.clientY;
    checkMouseOver(mx, my);
}

/* PRELOAD METHODS */
function loadQueries() {

}

/* SETUP METHODS */
function createBubbles() {
    for (let i = 0; i < 1; i++) {
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

function updateDots() {
    for (let i = 0; i < dots.length; i++) {
        ctx.fillStyle = 'white';
        ctx.fillRect(dots[i].x, dots[i].y, 3, 3);
    }
}

function showWindowSize() {
    if (SHOW_WINDOW_SIZE) {
        ctx.font = `${FONTS_SIZE_S}px ${FONT_FAMILY}`;
        ctx.fillStyle = 'white';
        ctx.fillText(`[${window.innerWidth} x ${window.innerHeight}]`, 10, window.innerHeight - 20);
    }
}

function handleMouseMove(event) {
    let mx = event.clientX;
    let my = event.clientY;
    if (SHOW_MOUSE_POSITION) {
        ctx.font = `${FONTS_SIZE_M}px ${FONT_FAMILY}`;
        ctx.fillStyle = 'white';
        ctx.fillText(`(${mx},${my})`, 10, window.innerHeight - 20);
    }
}

async function preload(callback) {
    console.log('preload');
    setTimeout(() => {
        callback();
    }, 500);
}

function setup() {
    console.log('setup');
    /* create entities */
    createBubbles();
}

function checkClick(mousePos) {
    dots.push(new Vector(mousePos.x, mousePos.y));
    for (let i = 0; i < bubbles.length; i++) {
        if (bubbles[i].isClicked(mousePos)) {
            console.log(bubbles[i].symbol);
            // bubbles.splice(i, 1);
            return;
        }
    }
}
  
function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    showWindowSize();
    // handleMouseMove();
    /* update entities */
    updateBubbles();

    updateDots();

    /* check mouse events */
    requestAnimationFrame(update);
}

function runGame() {
    console.log('runGame');
    setup();
    requestAnimationFrame(update);
}

preload(runGame);
